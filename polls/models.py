
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=50)

    def __str__(self):
        return f"User Entity : {self.first_name}+ {self.last_name}"


class Polls(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=50)
    description = models.TextField()

class Choices(models.Model):
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"Choice Entity : {self.text}"

class Vote(models.Model):
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE, related_name='votes')
    choice = models.ForeignKey(Choices, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('poll', 'choice'),)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} voted for {self.choice.text} in {self.poll.question}"