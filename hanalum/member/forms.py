from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User
import re


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '영문 + 숫자로 8자 이상'}))
    password2 = forms.CharField(label='비밀번호 재확인', widget=forms.PasswordInput(
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
        if is_match is None:  # 비밀번호가 정규식에 매치됨
            return "비밀번호는 8자리 이상 소문자+숫자"

        if password1 and password2 and password1 != password2:
            return "비밀번호가 일치하지 않습니다."
        return None

    def check_realname(self): # 실명확인
        return

    def check_email(self, _email):
        return User.objects.filter(email=_email).count()

    def save(self, commit=True):
        # 비밀번호를 해시 상태로 저장
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label='password')

    class Meta:
        model = User
        fields = ['email', 'password', 'nickname', 'realname', 'gender', 'is_active', 'is_admin']

    def clean_password(self):
        return self.initial["password"]
