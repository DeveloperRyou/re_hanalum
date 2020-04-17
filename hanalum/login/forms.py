from django import forms
from django.contrib import auth
from member.models import User


class UserLoginForm(forms.Form):
    email = forms.CharField(
        label='이메일',
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email address', 'autofocus': 'autofocus', 'id': 'user_id'}
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
        if user is not None:  # 로그인 성공
            auth.login(request, user)
            return user
        else:  # 유저가 없어서 / 이메일 인증이 안됨
            return

    def user_statement(self):
        statement = {'incorrect': False, 'uncertified_email': False}
        _email = self.cleaned_data.get("email")
        if User.objects.filter(email=_email).count() > 0:
            user = User.objects.get(email=_email)
            if user.is_active:
                statement['incorrect'] = True
            else:
                statement['uncertified_email'] = True
        else:
            statement['incorrect'] = True
        return statement
