from django.contrib import admin
from .models import User, Vote, Polls, Choices

# Register your models here.

admin.site.register(User)
admin.site.register(Polls)
admin.site.register(Choices)
admin.site.register(Vote)
