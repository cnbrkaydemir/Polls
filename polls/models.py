from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password']

    def __str__(self):
        return f"User Entity : {self.first_name} {self.last_name}"


    def has_perm(self, perm, obj=None):
        """Check if the user has a specific permission"""
        return True

    def has_module_perms(self, app_label):
        """Check if the user has permissions for the app"""
        return True

    @property
    def is_staff(self):
        """Admins are staff"""
        return self.is_admin


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, date_of_birth, gender):
        """Creates and saves a User with the given email, name, and password."""
        if not email:
            raise ValueError("Users must have an email address")

        if not first_name:
            raise ValueError("Users must have a first name")

        if not last_name:
            raise ValueError("Users must have a last name")

        if not password:
            raise ValueError("Users must have a password")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            is_active=True,
            is_admin=False,
        )
        user.set_password(password)  # Hashes password before saving
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Creates and saves a superuser"""
        user = self.create_user(email, first_name, last_name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user



class Polls(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
        unique_together = (('poll', 'choice'),)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} voted for {self.choice.text} in {self.poll.question}"