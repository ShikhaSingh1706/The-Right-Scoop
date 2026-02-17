from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import UserForm, UserProfileForm, AddressForm
from .models import Profile, AddressBook, Wishlist


# Create your views here.

class DashboardHomeView(LoginRequiredMixin,View):
    login_url = '/login-page/'

    def get(self,request):
        return render(request, 'user_dashboard/dashboard.html')


class ProfileView(LoginRequiredMixin,View):
    login_url = '/login-page/'

    def get(self, request):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        addresses = request.user.addresses.all()
        default_address = addresses.filter(is_shipping=True).first()


        return render(
            request,
            'user_dashboard/profile_view.html',
            {
                'profile': profile,
                'addresses': addresses,
                'default_address': default_address

            }
        )


class ProfileEditView(LoginRequiredMixin,View):
    login_url = '/login-page/'

    def get(self, request):
        profile = request.user.profile
        form = UserProfileForm(instance=profile)
        return render(request, 'user_dashboard/profile_edit.html', {'form': form})

    def post(self, request):
        profile = request.user.profile
        form = UserProfileForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard:profile_view')
        return render(request, 'user_dashboard/profile_edit.html', {'form': form, 'form': form})
    


class AddressListView(LoginRequiredMixin, View):
    def get(self, request):
        addresses = request.user.addresses.all()
        return render(
            request,
            'user_dashboard/address_list.html',
            {'addresses': addresses}
        )


class AddressAddView(LoginRequiredMixin,View):
    login_url='/login-page/'    

    def get(self,request):
        form=AddressForm()
        return render(request,'user_dashboard/address_add.html',{'form':form})
    
    def post(self,request):
        form=AddressForm(request.POST)


        if form.is_valid():
            address=form.save(commit=False)
            address.user=request.user
            address.save()
            messages.success(request,'Address added Successsfully')
            return redirect('dashboard:address_list')
        
        return render(request,'user_dashboard/address_add.html',{'form':form})
    

class AddressEditView(LoginRequiredMixin, View):
    login_url = '/login-page/'

    def get(self, request, pk):
        address = get_object_or_404(AddressBook, pk=pk, user=request.user)
        form = AddressForm(instance=address)
        return render(request, 'user_dashboard/address_edit.html', {'form': form})

    def post(self, request, pk):
        address = AddressBook.objects.get(pk=pk, user=request.user)
        form = AddressForm(request.POST, instance=address)

        if form.is_valid():
            form.save()
            messages.success(request, "Address updated successfully")
            return redirect('dashboard:address_list')

        return render(request, 'user_dashboard/address_edit.html', {'form': form})


class AddressDeleteView(LoginRequiredMixin, View):
    login_url = '/login-page/'  # Adjust if your login URL is different

    def get(self, request, pk):
        """
        Optional: show confirmation page
        """
        address = get_object_or_404(AddressBook, pk=pk, user=request.user)
        return render(request, 'user_dashboard/address_confirm_delete.html', {'address': address})

    def post(self, request, pk):
        """
        Actually delete the address
        """
        address = get_object_or_404(AddressBook, pk=pk, user=request.user)
        address.delete()
        messages.success(request, "Address deleted successfully")
        return redirect('dashboard:address_list')


class WishlistView(LoginRequiredMixin, View):
    def get(self, request):
        wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
        return render(
            request,
            'user_dashboard/wishlist.html',
            {'wishlist_items': wishlist_items}
        )

   