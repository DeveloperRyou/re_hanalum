from django.shortcuts import render
from .models import Sidebar

# Create your views here.

def main(request):
    return render(request, 'main.html')