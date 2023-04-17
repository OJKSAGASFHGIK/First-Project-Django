from django.http import HttpResponse
from django.shortcuts import render


def nothing(request):
    return HttpResponse('Hello... what do you want?!!')


def contact(request):
    return HttpResponse('My discord is Greque#7432')


def about(request):
    return HttpResponse('I like coffee!')

# Create your views here.
