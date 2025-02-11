from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.forms import RegistrationForm, LoginForm
from users.models import User

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date_of_birth = form.cleaned_data['date_of_birth']
            gender = form.cleaned_data['gender']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            if password != password2:
                context = {
                    'form' : form ,
                    'error':'Passwords must match!',
                }
                return render(request, "register.html", context)


            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, date_of_birth=date_of_birth, gender=gender)
            user.save()
            return redirect("login")

    form = RegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password =form.cleaned_data['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                context = {
                    'form': form,
                    'error':'Invalid Credentials!',
                }

                return render(request, 'login.html', context)

    form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('home')