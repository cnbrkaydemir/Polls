from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('poll_create/', views.create_poll, name='poll_create'),

    path('poll/<int:poll_id>/', views.get_poll_detail, name='poll_detail'),

]
