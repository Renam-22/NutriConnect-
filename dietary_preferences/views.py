from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DietaryPreference
from .forms import DietaryPreferenceForm

@login_required
def dietary_preferences_view(request):
    """View to handle dietary preferences."""
    try:
        preference = DietaryPreference.objects.get(user=request.user)
    except DietaryPreference.DoesNotExist:
        preference = None

    if request.method == 'POST':
        form = DietaryPreferenceForm(request.POST, instance=preference)
        if form.is_valid():
            pref = form.save(commit=False)
            pref.user = request.user
            pref.save()
            return redirect('dietary_success')  
    else:
        form = DietaryPreferenceForm(instance=preference)

    return render(request, 'preferences.html', {'form': form})


def dietary_success(request):
    return render(request, 'success.html')
