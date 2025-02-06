from django.urls import path

from poll_system.urls import urlpatterns
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
