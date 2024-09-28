from django.contrib import admin
from django.urls import path,include
from .views import first,demo

urlpatterns = [
    path('first/',first,name="first"),
    path('demo/', demo,name="demo")
]
