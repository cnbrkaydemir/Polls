from django.http import HttpResponse
from django.shortcuts import render, redirect

from polls.models import User


# Create your views here.

def home(request):
    return render(request, 'home.html')


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


        user = User(first_name=first_name, last_name=last_name, email=email, date_of_birth=date_of_birth, gender=gender)
        user.save()
        return redirect("home")

    return render(request, 'register.html')