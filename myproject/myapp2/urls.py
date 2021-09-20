from django.contrib import admin
from django.urls import path
from myapp2 import views

urlpatterns = [
    path("", views.demo, name="demo")
]
