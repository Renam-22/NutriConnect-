from django.urls import path,include
from django.conf import settings
from . import views
from meals.views import meal_suggestion
from consultations.views import book_appointment
from marketplace.views import product_list
from chatbot.views import list_messages

from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('meal/', meal_suggestion, name='meal_suggestion'), 
    path('consultation/', book_appointment, name='book_appointment'),  
    path('marketplace/', product_list, name='product_list'),
    path('detail/', views.detail ,name='detail'),
    path('chatbot/',list_messages,name='list_messages'),
    path('preferance/',include('dietary_preferences.urls')),
    path('profile/', views.update_profile_view, name='update_profile'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)