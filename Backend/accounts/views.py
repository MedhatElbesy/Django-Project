from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.db import transaction
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from accounts.models import User
from accounts.forms import RegisterForm
from accounts.tokens import account_activation_token
from accounts.serializers import LoginSerializer, RegisterSerializer
# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, "accounts/crud/index.html",
                    context={"users": users}, status=200)

def create(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "User Add Successfully.")
            return redirect("accounts.index")

    return render(request, "accounts/crud/create.html", {"form": form})

def edit(request, id):
    user = get_object_or_404(User, pk=id)
    form = RegisterForm(instance=user)

    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()

            messages.success(request, "User updated successfully.")
            return redirect("accounts.index")

    return render(request, 'accounts/crud/edit.html', context={"form": form})


def show(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, "accounts/crud/show.html", context={"user": user}, status=200)

def delete(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    url = reverse("users.index")
    messages.success(request, "User Deleted Successfully.")

    return redirect(url)

def profile(request):
    return render(request, "accounts/crud/show.html", status=200)

# Apis
@api_view(['POST'])
def login(request):     #login(TokenObtainPairView):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token_obtain_view = TokenObtainPairView.as_view()
                token_request = request._request
                token_response = token_obtain_view(token_request)
                token_data = token_response.data
                return Response({
                    'message': 'Login successfully',
                    'user': user.username,
                    'email': user.email,
                    'token': token_data['access'],
                    'refresh_token': token_data['refresh']
                })
            else:
                return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if request.method == "POST":
        try:
            with transaction.atomic():
                if serializer.is_valid():
                    if not User.objects.filter(email=serializer.validated_data['email']).exists():
                        user = serializer.save()
                        user.is_active = False
                        user.save()

                        current_site = get_current_site(request)    # get url of site
                        mail_subject = 'Verify your email address'
                        message = render_to_string('registration/verify_email.html', {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token': account_activation_token.make_token(user),
                        })
                        to_email = serializer.validated_data.get('email')
                        email = EmailMessage(mail_subject, message, to=[to_email])
                        email.content_subtype = "html"
                        email.send()
                        return JsonResponse({'message': 'Please confirm your email address to complete the registration'})
                    return Response({'error': 'User already exists, use another email address or login'}, status=status.HTTP_400_BAD_REQUEST)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return Response({'error': 'An error occurred. Please try again later.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'error': 'Invalid URL'}, status=status.HTTP_400_BAD_REQUEST)

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return JsonResponse({'message': 'Your email address has been verified. Now you can login to your account.'}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Activation link is invalid!'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = RegisterSerializer(request.user)
    return Response(user.data)
