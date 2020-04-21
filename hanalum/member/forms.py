from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, ReadOnlyPasswordHashField
from .models import User
import re

from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.encoding import force_bytes


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '영문 + 숫자로 8자 이상'}))
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '영문 + 숫자로 8자 이상'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'nickname', 'realname', 'gender', 'admission_year']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@hanalum.kr'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '입력하세요'}),
            'realname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '입력하세요'}),
            'gender': forms.Select(attrs={'class': 'form-control', }),
            'admission_year': forms.Select(attrs={'class': 'form-control', })
        }
        labels = {
            'email': '이메일',
            'nickname': '닉네임',
            'realname': '실명',
            'gender': '성별',
            'admission_year': '입학년도',
        }

    def check_password(self): # 비밀번호 확인
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        p = re.compile("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
        is_match = p.match(password1)  # 여기에 비밀번호 정규식
        if is_match is None:  # 비밀번호가 정규식에 매치되지 않음
            return "비밀번호는 8자리 이상 소문자+숫자"

        if password1 and password2 and password1 != password2:
            return "비밀번호가 일치하지 않습니다."
        return ""

    def check_realname(self, _realname): # 실명확인
        p = re.compile("^[가-힣]+$")
        is_match = p.match(_realname)
        if is_match is None:
            return "한글 실명을 입력하세요."
        return ""

    def check_email(self, _email):
        return User.objects.filter(email=_email).count()

    def check_nickname(self, _nickname):
        return User.objects.filter(nickname=_nickname).count()

    def save(self, current_site, mail_to, commit=True):
        # 비밀번호를 해시 상태로 저장
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.is_active = False
            user.save()
            message = render_to_string('activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_title = "한아름 계정 활성화 확인 이메일"
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.content_subtype = "html"
            email.send()

        return user


class CustomUserChangeForm(UserChangeForm):
    password = None
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '영문 + 숫자로 8자 이상'}))
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '영문 + 숫자로 8자 이상'}))

    class Meta:
        model = User
        fields = ['avatar', 'nickname', 'password1', 'password2']
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'custom-file-input'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '입력하세요'}),
        }
        labels = {
            'avatar': '프로필',
            'nickname': '닉네임',
        }

    def check_password(self): # 비밀번호 확인
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        p = re.compile("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
        is_match = p.match(password1)  # 여기에 비밀번호 정규식
        if is_match is None:  # 비밀번호가 정규식에 매치되지 않음
            return "비밀번호는 8자리 이상 소문자+숫자"

        if password1 and password2 and password1 != password2:
            return "비밀번호가 일치하지 않습니다."
        return ""

    def check_nickname(self, user_nickname, _nickname):
        if user_nickname == _nickname:
            return 0
        return User.objects.filter(nickname=_nickname).count()

    def save(self, commit=True):
        # 비밀번호를 해시 상태로 저장
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class CustomPasswordChageform(PasswordChangeForm):
    pass
