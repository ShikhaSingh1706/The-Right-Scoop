from django.urls import path
from .views import DashboardHomeView, ProfileView, ProfileEditView

app_name = 'dashboard'   # important for namespacing

urlpatterns = [
    path('', DashboardHomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile_view'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
]
