from django.urls import path
from Recipes.views import home

urlpatterns = [
    path('', home),
]
