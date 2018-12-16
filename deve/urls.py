

from django.contrib import admin
from django.urls import path
from .import view

urlpatterns = [
    path('', view.login),
    path('count', view.count, name='count')
]
