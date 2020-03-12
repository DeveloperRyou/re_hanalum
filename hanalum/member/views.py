from django.shortcuts import render
from .forms import UserCreationForm
from django.shortcuts import redirect


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            is_error = form.check_password2()
            if is_error is None:
                form.save()
                return redirect('login')
            else:
                return render(request, 'register.html', {'form': form, 'error': is_error})
        else:
            return redirect('register')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


def agree(request):
    return render(request, 'agree.html')

