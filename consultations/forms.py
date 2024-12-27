from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'nutritionist']  # Adjust fields as necessary
        widgets = {
            'date': forms.SelectDateWidget(),  # For date selection
        }
