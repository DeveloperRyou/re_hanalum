from django.shortcuts import render
from .forms import UserLoginForm
from django.shortcuts import redirect
from django.contrib import auth


# Create your views here.
def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            if user:
                return redirect('main')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('main')
        form = UserLoginForm()
        return render(request, 'login.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('login')
