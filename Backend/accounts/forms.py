from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from accounts.models import User
from django.core.validators import MinLengthValidator

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    first_name = forms.CharField(required=True, max_length=150, validators=[MinLengthValidator(2)])
    last_name = forms.CharField(required=True, max_length=150,  validators=[MinLengthValidator(2)])

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'mobile_phone', 'profile_image')

    def clean_email(self):
        email = self.cleaned_data['email']
        email_found = User.objects.filter(email=email).exists()
        if email_found:
            raise forms.ValidationError('Email address is already used, please choose another one')
        return email













# def RegisterForm(UserCreationForm):
#     if UserCreationForm.is_valid():
#         user = UserCreationForm
#         user.set_password(
#             UserCreationForm.cleaned_data["password"]
#         )
#
#
# from django import forms
# from django.contrib.auth.models import User
#
#
# class RegisterationForm(UserCreationForm):
#     class Meta:
#         model = User
#         # fields = '__all__'
#         fields = ('username', 'password1','password2', 'first_name', 'last_name', 'email')
#
#         email = forms.EmailField(
#             label=_("Email"),
#             max_length=254,
#             widget=forms.EmailInput(attrs={"autocomplete": "email"}),
#         )
#         username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
#
#         new_password2 = forms.CharField(
#             label=_("New password confirmation"),
#             strip=False,
#             widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
#         )
#
#         old_password = forms.CharField(
#             label=_("Old password"),
#             strip=False,
#             widget=forms.PasswordInput(
#                 attrs={"autocomplete": "current-password", "autofocus": True}
#             ),
#         )