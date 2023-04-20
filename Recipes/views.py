from django.shortcuts import render


def home(request):
    return render(request, 'recipes/a1pages/a1home.html', context={
        'name': 'Recipes'
    })

# Create your views here.
