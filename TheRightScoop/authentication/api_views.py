from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from TheRightScoop.api_response.custom_response_handler import APIResponse


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

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
    
class LoginView(APIView):
    permission_classes=[AllowAny]   

    def post(self,request):
        username=request.data.get ("username")
        password=request.data.get("password")

        if not username or not password:
            return APIResponse.error(
                message="Username and password are required",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        user=authenticate(username=username,password=password)
        
        if user is not None:
            refresh=RefreshToken.for_user(user)
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
        else:
            return APIResponse.error(
                message="Invalid credentials",
                status_code=status.HTTP_401_UNAUTHORIZED
            )
