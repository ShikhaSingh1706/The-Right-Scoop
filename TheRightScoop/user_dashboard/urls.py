from django.urls import path
from .views import DashboardHomeView, ProfileView, ProfileEditView, AddressAddView,AddressListView, AddressEditView, WishlistView, AddressDeleteView


app_name = 'dashboard'   # important for namespacing

urlpatterns = [
    path('', DashboardHomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile_view'),
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('address_list/',AddressListView.as_view(), name='address_list'),
    path('address/add/',AddressAddView.as_view(), name='address_add'),
    path('address/<int:pk>/edit/',AddressEditView.as_view(), name='address_edit'),
    path('address/<int:pk>/delete/', AddressDeleteView.as_view(), name='address_delete'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),

    

]
