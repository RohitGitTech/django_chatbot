# chatbot_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chatbot', views.chat, name='chat'),
]
