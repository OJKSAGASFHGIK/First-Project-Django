from utils.recipes.factory import make_recipe

from django.shortcuts import render


def home(request):
    return render(request, 'recipes/a1pages/a1home.html', context={
        'name': 'Recipes',
        'recipes': [make_recipe() for _ in range(6)],
    })


def recipe(request, id):
    return render(request, 'recipes/a1pages/a2recipeView.html', context={
        'recipe': make_recipe(),
        'a1': True,  # texto grandão
    })

# Create your views here.
