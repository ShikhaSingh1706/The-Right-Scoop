from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .forms import CategoryForm

def is_admin(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(is_admin)
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Category successfully added!")

            return redirect('category:category_add')
    else:
        form = CategoryForm()

    return render(request, 'category/add_category.html', {'form': form})
