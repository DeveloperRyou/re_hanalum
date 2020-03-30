from django.shortcuts import render
from .forms import UserCreationForm
from django.shortcuts import redirect


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        nickname_error = ""
        email_error = ""

        if form.check_nickname(request.POST['nickname']) > 0:
            nickname_error = "이미 사용중인 닉네임입니다."
        if form.check_email(request.POST['email']) > 0:
            email_error = "이미 등록된 이메일입니다."

        if nickname_error == "" and email_error == "":  # 닉네임과 이메일 모두 사용가능한경우
            if form.is_valid():
                is_error = form.check_password()
                realname_error = form.check_realname(request.POST['realname'])
                if (is_error == "") and (realname_error == ""):
                    form.save()
                    return redirect('login')
                else:
                    return render(request, 'register.html', {'form': form, 'password2_error': is_error, 'realname_error': realname_error})
            else:
                return redirect('register')
        else:  # 닉네임, 이메일 둘중 하나라도 중복인경우
            return render(request, 'register.html', {'form': form, 'nickname_error': nickname_error, 'email_error': email_error})


    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


def agree(request):
    return render(request, 'agree.html')

