from django import forms
from member.models import User
from django.contrib import auth


class UserLoginForm(forms.Form):
    email = forms.CharField(
        label='이메일',
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email address', 'autofocus':'autofocus', 'id': 'user_id'}
        )
    )
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}
        )
    )

    class Meta:
        fields = ['email', 'password']

    def login(self, request):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = auth.authenticate(request, username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return user
        else:
            return
            #raise forms.ValidationError("비밀번호가 일치하지 않습니다")

