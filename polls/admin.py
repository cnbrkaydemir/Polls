from django.contrib import admin
from .models import Vote, Polls, Choices

# Register your models here.

admin.site.register(Polls)
admin.site.register(Choices)
admin.site.register(Vote)
