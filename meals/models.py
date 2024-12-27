from django.db import models
from users.models import CustomUser

class meal_plan(models.Model): 
    user = models.ForeignKey(CustomUser, verbose_name="user", on_delete=models.CASCADE)
    meal = models.CharField(max_length=100)

    def __str__(self):
        return f"Meal Plan for {self.user.username}"