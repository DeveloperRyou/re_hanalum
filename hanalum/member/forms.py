from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '영문 + 숫자로 8자 이상'}))
    password2 = forms.CharField(label='비밀번호 재확인', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '영문 + 숫자로 8자 이상'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'nickname', 'realname', 'sex', 'admission_year']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@hanalum.kr'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '입력하세요'}),
            'realname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '입력하세요'}),
            'sex': forms.Select(attrs={'class': 'form-control', }),
            'admission_year': forms.Select(attrs={'class': 'form-control', })
        }
        labels = {
            'email': '이메일',
            'nickname': '닉네임',
            'realname': '실명',
            'sex': '성별',
            'admission_year': '입학년도',
        }

    def check_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다")
        return password2

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
        fields = ['email', 'password', 'nickname', 'realname', 'sex', 'is_active', 'is_admin']

    def clean_password(self):
        return self.initial["password"]