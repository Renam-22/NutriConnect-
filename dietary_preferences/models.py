from django.db import models
from users.models import CustomUser

class DietaryPreference(models.Model):
    DIETARY_RESTRICTIONS = [
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('gluten_free', 'Gluten-Free'),
        ('lactose_free', 'Lactose-Free'),
        ('nut_allergy', 'Nut Allergy'),
    ]

    CUISINE_CHOICES = [
        ('italian', 'Italian'),
        ('mexican', 'Mexican'),
        ('japanese', 'Japanese'),
        ('indian', 'Indian'),
    ]

    user = models.ForeignKey(CustomUser, verbose_name="user", on_delete=models.CASCADE)
    restrictions = models.JSONField(default=list)  
    cuisines = models.JSONField(default=list)     

    def __str__(self):
        return f"{self.user.username}'s Preferences"
