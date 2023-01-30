from django.contrib import admin
from django.urls import path
from .views import SighUpView



urlpatterns = [
    path('signup', SighUpView.as_view(), name='accounts-signup')
]