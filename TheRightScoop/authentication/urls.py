from django.urls import path
from .api_views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register_page, login_page


urlpatterns = [
    # Frontend HTML pages
    path('register-page/', register_page, name='register-page'),
    path('login-page/', login_page, name='login-page'),

# Backend API URLs
    path('api/register/',RegisterView.as_view(),name='register'),
    path('api/login/',LoginView.as_view(),name='login'),
    path('api/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]
