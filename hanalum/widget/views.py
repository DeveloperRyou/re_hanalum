from django.shortcuts import render


# Create your views here.
def calendar(request):
    return render(request,'calendar.html')


def cafeteria(request):
    return render(request, 'cafeteria.html')


def acadnotice(request):
    return render(request, 'acadnotice.html')