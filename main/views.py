from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def intro(request):
    return render(request, 'main/main.html')

def about(request):
    return render(request, 'main/about.html')