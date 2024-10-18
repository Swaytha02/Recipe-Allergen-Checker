from django.contrib import admin
from .models import Allergen, Ingredient, Recipe

# Register your models here.
admin.site.register(Allergen)
admin.site.register(Ingredient)
admin.site.register(Recipe)

