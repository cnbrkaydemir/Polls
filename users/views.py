from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.models import User

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, "register.html", {"error": "Passwords do not match!"})


        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password1, date_of_birth=date_of_birth, gender=gender)
        user.save()
        return redirect("login")

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Password or Email is incorrect!"
            return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('home')