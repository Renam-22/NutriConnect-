from django.urls import path
from .views import dietary_preferences_view,dietary_success

urlpatterns = [
    path('', dietary_preferences_view, name='dietary_preferences_view'),
    path('success/', dietary_success, name='dietary_success'),
]
