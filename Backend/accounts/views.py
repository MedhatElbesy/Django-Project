from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import JsonResponse, HttpResponseRedirect
from django.db import transaction
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from accounts.models import User
from accounts.forms import RegisterForm, UpdateUserForm
from accounts.tokens import token_generator
from accounts.serializers import LoginSerializer, RegisterSerializer, UserSerializer

import os       # for use .env -> python-dotenv

# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, "accounts/crud/index.html",
                    context={"users": users}, status=200)

def create(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, "User Add Successfully.")
            return redirect("accounts.index")
    return render(request, "accounts/crud/create.html", {"form": form})

def edit(request, id):
    user = get_object_or_404(User, pk=id)

    if request.method == "POST":
        form = UpdateUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully.")
            return redirect("accounts.index")
    else:
        form = UpdateUserForm(instance=user)

    return render(request, 'accounts/crud/edit.html', context={"form": form})


def show(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, "accounts/crud/show.html", context={"user": user}, status=200)

def delete(request, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    url = reverse("accounts.index")
    messages.success(request, "User Deleted Successfully.")

    return redirect(url)

def admin_profile(request):
    return render(request, "accounts/admin_profile.html", status=200)

# Apis
@api_view(['POST'])
def login(request):     #login(TokenObtainPairView):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
            if user:
                token_obtain_view = TokenObtainPairView.as_view()
                token_request = request._request
                token_response = token_obtain_view(token_request)
                token_data = token_response.data

                user_serializer = UserSerializer(user)  # Serialize the user object
                print(user_serializer.data)
                request.session['user'] = user_serializer.data
                request.session.set_expiry(3600) # Set session expiry to 1 hour
                print(request.session['user'])
                return Response({
                    'message': 'Login successfully',
                    'user': user_serializer.data,
                    'email': user.email,
                    'token': token_data['access'],
                    'refresh_token': token_data['refresh']
                })
                #response.set_cookie('token', token_data['access'], max_age=3600, secure=True,httponly=True)
            else:
                return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
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
                            'token': token_generator.make_token(user),
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

@api_view(['GET'])
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        frontend_host = os.getenv('FRONTEND_HOST', 'http://localhost:8080')
        message = "Your email address has been verified. Now you can login to your account."
        status = 200
        print("Your email address has been verified. Now you can login to your account.")
        return HttpResponseRedirect(f"{frontend_host}/login?message={message}&status={status}")
    else:
        frontend_host = os.getenv('FRONTEND_HOST', 'http://localhost:8080')
        message = "Activation link is invalid!"
        status = 400
        print("Error, Activation link is invalid!")
        return HttpResponseRedirect(f"{frontend_host}/login?message={message}&status={status}")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = RegisterSerializer(request.user)
    return Response(user.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    if request.method == 'POST':
        serializer = UserSerializer(instance=request.user, data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user_serializer = UserSerializer(user)  # Serialize the user object
            request.session['user'] = user_serializer.data,
            request.session.set_expiry(3600)  # Set session expiry to 1 hour
            print(request.session['user'])
            return Response({'message': 'Profile updated successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@api_view(['POST'])
def forget_password(request):
    email = request.data.get('email')
    user = User.objects.filter(email=email).first()
    if user:
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user),

        current_site = get_current_site(request)
        mail_subject = 'Password reset requested'
        message = render_to_string('registration/password_reset_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': uid,
            'token': token,
        })
        to_email = email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.content_subtype = "html"
        email.send()

        return Response({'message': 'Password reset email sent'})
    else:
        return Response({'error': 'User not found with this email'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def reset_password(request, token):
    new_password = request.data.get('new_password')
    user = User.objects.filter(password_reset_token=token).first()
    if user:
        user.set_password(new_password)
        user.password_reset_token = None  # Clear the reset token
        user.save()
        return Response({'message': 'Password reset successful'})
    else:
        return Response({'error': 'Invalid or expired token'}, status=400)

#
# def reset_password(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#
#     if user and PasswordResetTokenGenerator().check_token(user, token):
#         if request.method == 'POST':
#             # Handle form submission
#             new_password = request.POST.get('new_password')
#             user.set_password(new_password)
#             user.save()
#             # Redirect to password reset success page
#             return redirect('password_reset_success')
#         else:
#             # Render password reset form
#             return render(request, 'reset_password.html')
#     else:
#         # Invalid token or user not found
#         return render(request, 'invalid_reset_link.html')
