from django.shortcuts import render
from .forms import UserCreationForm, CustomUserChangeForm
from django.shortcuts import redirect
from django.contrib.auth import update_session_auth_hash
from .models import User
from django.contrib import auth
from login.forms import UserLoginForm
from board.models import Board
from article.models import Article

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
        nickname_error = form.check_nickname(request.POST['nickname'])  # "" 일 경우 사용 가능함
        email_error = form.check_email(request.POST['email'])

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


def agree(request):
    return render(request, 'agree.html')


def memberinfo(request):
    
    # 메뉴
    category = Board.objects.all().order_by('-priority')

    try:
        notice_cnt = 3
        board_notice_type = Board.objects.get(board_id='notice')
        notice = Article.objects.filter(board_type=board_notice_type).order_by('-created_at')[:notice_cnt]
    except:
        notice = None
    
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        nickname_error = form.check_nickname(request.POST['nickname'], request.user.nickname)

        if nickname_error is None:  # 닉네임 사용가능한경우
            if form.is_valid():
                is_error = form.check_password()
                if is_error == "":
                    user = form.save()
                    update_session_auth_hash(request, user)
                    return redirect('main')
                else:
                    return render(request, 'memberinfo.html', {'category': category, 'form': form, 'password2_error': is_error, 'notice': notice})
            else:
                return redirect('register')
        else:  # 닉네임 중복인경우
            return render(request, 'memberinfo.html', {'category': category, 'form': form, 'nickname_error': nickname_error , 'notice': notice})

    else:
        form = CustomUserChangeForm(instance=request.user)
        return render(request, 'memberinfo.html', {'category': category, 'form': form, 'notice': notice})


def memberdelete(request):
    if request.method == 'POST':
        user = auth.authenticate(request, username=request.user.email, password=request.POST['password'])

        if user is not None: # 맞은 경우
            user.delete()
            return redirect('login')

        else:
            return redirect('memberinfo')