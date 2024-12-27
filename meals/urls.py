from django.urls import path
from .views import meal_check

urlpatterns = [
    path('', meal_check, name='meal_check'),
]
