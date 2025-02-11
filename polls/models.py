from datetime import datetime

from django.db import models
from users.models import User


class Polls(models.Model):
    created_user = models.IntegerField(default=0)
    question = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())

class Choices(models.Model):
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return f"Choice Entity : {self.text}"

class Vote(models.Model):
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE, related_name='votes')
    choice = models.ForeignKey(Choices, on_delete=models.CASCADE, related_name='choice_votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')

    class Meta:
        unique_together = (('poll', 'choice', 'user'),)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} voted for {self.choice.text} in {self.poll.question}"