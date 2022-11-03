from django.urls import path
from Recipes.views import about, contact, nothing

urlpatterns = [
    path('', nothing),
    path('contact/', contact),
    path('about/', about),
]
