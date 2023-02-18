from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def photo(request):
    return render(request, 'photos.html')