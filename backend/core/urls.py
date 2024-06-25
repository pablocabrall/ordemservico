from django.contrib import admin
from django.urls import path
from backend.core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index')
]
