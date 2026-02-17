import json
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from TheRightScoop.api_response.custom_response_handler import APIResponse


class RegisterView(View):

    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):

        # -------- API REGISTER (JSON) --------
        if request.headers.get("Content-Type", "").startswith("application/json"):
            data = json.loads(request.body)

            serializer = RegisterSerializer(data=data)
            if serializer.is_valid():
                user = serializer.save()
                return APIResponse.success(
                    data={
                        "id": user.id,
                        "username": user.username,
                        "email": user.email
                    },
                    message="User registered successfully",
                    status_code=status.HTTP_201_CREATED
                )

            return APIResponse.error(
                message="Validation failed",
                errors=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )

        # -------- FRONTEND REGISTER (FORM) --------
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Registration successful")
        return redirect("login")


class LoginView(View):

    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):

        # -------- API LOGIN (JSON) --------
        if request.headers.get("Content-Type", "").startswith("application/json"):
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                return APIResponse.error(
                    message="Username and password are required",
                    status_code=status.HTTP_400_BAD_REQUEST
                )

            user = authenticate(username=username, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                return APIResponse.success(
                    data={
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "access": str(refresh.access_token),
                        "refresh": str(refresh)
                    },
                    message="Login successful",
                    status_code=status.HTTP_200_OK
                )

            return APIResponse.error(
                message="Invalid credentials",
                status_code=status.HTTP_401_UNAUTHORIZED
            )

        # -------- FRONTEND LOGIN (FORM) --------
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("dashboard:home")

        messages.error(request, "Invalid username or password")
        return redirect("login")
