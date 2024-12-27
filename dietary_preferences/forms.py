from django import forms
from .models import DietaryPreference

class DietaryPreferenceForm(forms.ModelForm):
    class Meta:
        model = DietaryPreference
        fields = ['restrictions', 'cuisines']

    restrictions = forms.MultipleChoiceField(
        choices=DietaryPreference.DIETARY_RESTRICTIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Dietary Restrictions",
    )

    cuisines = forms.MultipleChoiceField(
        choices=DietaryPreference.CUISINE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Cuisine Preferences",
    )
