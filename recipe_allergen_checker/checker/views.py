import logging
from django.shortcuts import render
from .models import Recipe, Allergen

logger = logging.getLogger('checker')  # Use your app-specific logger

def recipe_list(request):
    recipes = Recipe.objects.all()
    allergens = Allergen.objects.all()
    selected_allergens = request.GET.getlist('allergens')

    logger.debug(f"Selected Allergens: {selected_allergens}")  # Debugging line

    if selected_allergens:
        selected_allergens = [int(id) for id in selected_allergens]
        logger.debug(f"Filtered Allergens IDs: {selected_allergens}")  # Debugging line
        recipes = recipes.exclude(ingredients__allergens__id__in=selected_allergens).distinct()
        logger.debug(f"Filtered Recipes: {recipes}")  # Debugging line

    context = {
        'recipes': recipes,
        'allergens': allergens,
        'selected_allergens': selected_allergens,
    }
    return render(request, 'checker/recipe_list.html', context)
