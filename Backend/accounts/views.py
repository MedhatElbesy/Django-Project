from django.shortcuts import render, redirect, reverse, get_object_or_404
from accounts.forms import RegisterForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from accounts.serializers import LoginSerializer
from accounts.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, "accounts/crud/index.html",
                    context={"users": users}, status=200)

def create(request):
    form = RegisterForm()
    if request.method == "POST":
        form= RegisterForm(request.POST)
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
