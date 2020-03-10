from django.shortcuts import render


# Create your views here.
def register(request):
    return render(request, 'register.html')

def agree(request):
    return render(request, 'agree.html')