from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Use '' instead of ' ' for the root URL
]
