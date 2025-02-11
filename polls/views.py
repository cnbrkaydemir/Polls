from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from polls.models import Polls, Choices, Vote
from polls.forms import PollForm


def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def dashboard(request):
    polls = Polls.objects.all()
    user = request.user
    context = {'polls': polls, user: user}
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def create_poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        user = request.user

        if form.is_valid():
            poll = Polls(question=form.cleaned_data["question"], description=form.cleaned_data["description"], created_user=user.id)
            poll.save()

            options = [form.cleaned_data["option1"], form.cleaned_data["option2"],
                       form.cleaned_data["option4"], form.cleaned_data["option4"]]

            for option in options:
                if option.strip():
                    choice = Choices(text=option, poll=poll, votes=0)
                    choice.save()

            return redirect('dashboard')

    form = PollForm()
    context = {'form': form}

    return render(request, "poll_create.html", context)

@login_required(login_url='login')
def get_poll_detail(request, poll_id):
    poll = get_object_or_404(Polls, pk=poll_id)
    user = request.user
    voted = Vote.objects.filter(user=user, poll=poll).count() >= 1
    user_choice = Vote.objects.filter(user=user, poll= poll).first().choice if voted else None
    completion = False

    if request.method == "POST":
        choice_id = request.POST.get("option")
        user_choice = get_object_or_404(Choices, id=choice_id)
        user_choice.votes += 1
        user_choice.save()

        vote = Vote(user=user, choice=user_choice, poll=poll)
        vote.save()
        voted = True
        completion = True

    context = {"poll": poll, "voted": voted, "user_choice":user_choice, "completion":completion}

    return render(request, "poll_detail.html",context)

