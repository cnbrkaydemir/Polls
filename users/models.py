from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

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
            username=self.normalize_email(email),
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



class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

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

    objects = UserManager()





