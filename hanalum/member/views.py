from django.shortcuts import render
from .forms import UserCreationForm
from django.shortcuts import redirect


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid() and form.check_password2():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
