from django.http import HttpResponse
from django.shortcuts import render, redirect

from polls.models import User, Polls, Choices


# Create your views here.

def home(request):
    return render(request, 'home.html')


def dashboard(request):
    polls = Polls.objects.all()
    return render(request, 'dashboard.html', {'polls': polls})


def create_poll(request):
    if request.method == 'POST':
        question = request.POST['question']
        description = request.POST['description']
        user = User.objects.all()[0]

        poll = Polls(question=question, description=description, user=user)
        poll.save()

        options = [request.POST['option1'], request.POST['option2'], request.POST['option3'], request.POST['option4']]


        for option in options:
            if option != '':
                choice = Choices(text=option, poll=poll, votes=0)
                choice.save()

        poll.save()

        return redirect('dashboard')


    return render(request, "poll_create.html")


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
        return redirect("dashboard")

    return render(request, 'register.html')