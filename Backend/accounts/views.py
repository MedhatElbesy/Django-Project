from django.shortcuts import render, redirect, reverse, get_object_or_404
from accounts.forms import RegisterForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from accounts.serializers import LoginSerializer
from accounts.models import User
from django.contrib import messages

from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

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
class login(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                return Response({'message': 'Login successfully', 'user': user.username, 'email': user.email}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'Verify your email address'
            message = render_to_string('registration/verify_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.content_subtype = "html"
            email.send()

            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = RegisterForm()
    return render(request, "accounts/crud/create.html", {"form": form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Your email address has been verified. Now you can login to your account.')
    else:
        return HttpResponse('Activation link is invalid!')