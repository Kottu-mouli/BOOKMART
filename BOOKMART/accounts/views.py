from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/')  # Redirect to home or dashboard
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')
    else:
         return render(request, 'login.html')
    
  # Redirect to login page after logout


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not all([first_name, last_name, username, email, password, confirm_password]):
            messages.info(request, "All fields are required")
            return redirect('register')

        if password != confirm_password:
            messages.info(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already exists")
            return redirect('register')

        # If all checks pass
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, "Registration successful")
        return redirect('login')

    # Always return something on GET
    return render(request, 'register.html')

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def custom_logout_view(request):
    logout(request)
    return redirect('/')  # or redirect to home page or any other URL name

def contact(request):
    if request.method == 'POST':
        # Handle form submission here
        pass  # Replace with your form handling logic

    return render(request, 'contact.html')  # Assuming you have a contact.html template
