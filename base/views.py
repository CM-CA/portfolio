from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def home(request):
    return render(request, 'base/index.html')


def blog(request):
    return render(request, 'base/under_construction.html')
