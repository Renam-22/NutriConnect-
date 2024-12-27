from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user  
            appointment.save()
            return redirect('home')  
    else:
        form = AppointmentForm()
    return render(request, 'consultations/book_appointment.html', {'form': form})
