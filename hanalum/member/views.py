from django.shortcuts import render
from .forms import UserCreationForm, CustomUserChangeForm
from django.shortcuts import redirect
from django.contrib.auth import update_session_auth_hash
from .models import User
from django.contrib import auth
from login.forms import UserLoginForm

# SMTP 관련 인증
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text


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
                if (is_error == "") and (realname_error == ""):  # 회원가입 성공
                    current_site = get_current_site(request)
                    form.save(current_site, request.POST['email'])
                    form = UserLoginForm()
                    return render(request, 'login.html', {'form': form, 'registered': True})
                else:
                    return render(request, 'register.html', {'form': form, 'password2_error': is_error, 'realname_error': realname_error})
            else:
                return redirect('register')
        else:  # 닉네임, 이메일 둘중 하나라도 중복인경우
            return render(request, 'register.html',
                          {'form': form, 'nickname_error': nickname_error, 'email_error': email_error})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


# 계정 활성화 함수(토큰을 통해 인증)
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect("login")
    else:
        return redirect("login")
    return


def agree(request):
    return render(request, 'agree.html')


def memberinfo(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        nickname_error = ""

        if form.check_nickname(request.POST['nickname']) > 0:
            nickname_error = "이미 사용중인 닉네임입니다."

        if nickname_error == "":  # 닉네임과 이메일 모두 사용가능한경우
            if form.is_valid():
                is_error = form.check_password()
                if is_error == "":
                    user = form.save()
                    update_session_auth_hash(request, user)
                    return redirect('main')
                else:
                    return render(request, 'memberinfo.html', {'form': form, 'password2_error': is_error})
            else:
                return redirect('register')
        else:  # 닉네임 중복인경우
            return render(request, 'memberinfo.html', {'form': form, 'nickname_error': nickname_error})

    else:
        form = CustomUserChangeForm(instance=request.user)
        return render(request, 'memberinfo.html', {'form': form})
