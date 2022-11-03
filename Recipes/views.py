from django.http import HttpResponse
from django.shortcuts import render


def nothing(ItsArequest):
    return HttpResponse('Hello... what do you want?!!')


def contact(YeapArequest):
    return HttpResponse('My discord is Greque#7432')


def about(OhYesARequestttt):
    return HttpResponse('I like coffee!')

# Create your views here.
