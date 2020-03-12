from django.shortcuts import render
from .forms import UserLoginForm
from django.shortcuts import redirect


# Create your views here.
def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            if user:
                return redirect('article')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        form = UserLoginForm()
        return render(request, 'login.html', {'form':form})
