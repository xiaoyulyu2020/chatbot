from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('main/', views.chatbot, name="main"),
]
