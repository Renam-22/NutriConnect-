from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from nutri_connect.settings import GENERATIVEAI_API_KEY
from meals.models import meal_plan
import google.generativeai as genai
from users.forms import CustomUserCreationForm

def configure_genai():
    """Configure Generative AI API."""
    genai.configure(api_key=GENERATIVEAI_API_KEY)
    return genai.GenerativeModel("gemini-pro")

def generate_nutrition_prompt(user):
    """Generate a personalized nutrition prompt for the user."""
    prompt = f"""
    Generate a personalized nutrition plan based on the following user data:
    Name: {user.get('name')}
    Age: {user.get('age')}
    Weight: {user.get('weight')} kg
    Height: {user.get('height')} cm
    BMI: {user.get('bmi'):.2f}
    Primary Goal: {user.get('goal')}

    Please provide:
    1. Daily calorie target
    2. Macronutrient split (protein, carbs, fat)
    3. List of recommended foods
    4. Sample meal plan for one day
    """
    return prompt

@login_required
def generate_nutrition_plan(request):
    """Generate a nutrition plan based on user data."""
    user = request.user
    diet = user.dietarypreference

    user_data = {
        'name': "User" or user.username,
        'age': getattr(user, 'age', 0),
        'weight': getattr(user, 'weight', 0),
        'height': getattr(user, 'height', 0),
        'bmi': getattr(user, 'bmi', 0),
        'goal': getattr(user, 'goal'),
        'DIETARY_RESTRICTIONS': diet.restrictions,
        'CUISINE_CHOICES': diet.cuisines,
    }
    return generate_nutrition_prompt(user_data)

@login_required
def meal_suggestion(request):
    """Suggest a meal plan using Generative AI."""
    configure_genai()
    model = configure_genai()

    prompt = generate_nutrition_plan(request)

    bot_response = model.generate_content(prompt)

    meal_plan_instance = meal_plan.objects.create(user=request.user, meal=bot_response.text)

    return render(request, 'meal_plan.html', {
        'user': request.user,
        'meal_plan': meal_plan_instance,
    })

@login_required
def meal_check(request):
    """Check if a meal plan exists; if not, suggest one."""
    existing_meal_plan = meal_plan.objects.filter(user=request.user).last()

    if existing_meal_plan:
        return render(request, 'meal_plan.html', {
            'user': request.user,
            'meal_plan': existing_meal_plan,
        })

    return meal_suggestion(request)
