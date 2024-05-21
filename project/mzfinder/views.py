from django.shortcuts import render
from .models import Restaurant

def index(request):
    return render(request, 'mzfinder/mainPage.html')
def korean(request):
    return render(request, 'mzfinder/korean.html')