from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def intro(request):
    return render(request, 'main.html')