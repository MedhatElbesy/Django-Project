from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from accounts.models import User
from django.core.validators import MinLengthValidator

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=254, help_text='Required',
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
        if email:
            # Retrieve the current user instance from the form's instance attribute
            instance = getattr(self, 'instance', None)
            if instance and instance.pk:
                # Exclude the current user from the uniqueness check
                existing_user = User.objects.filter(email=email).exclude(pk=instance.pk).first()
            else:
                existing_user = User.objects.filter(email=email).first()

            if existing_user:
                raise forms.ValidationError('Email address is already used, please choose another one')

        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if username:
            # Retrieve the current user instance from the form's instance attribute
            instance = getattr(self, 'instance', None)
            if instance and instance.pk:
                # Exclude the current user from the uniqueness check
                existing_user = User.objects.filter(username=username).exclude(pk=instance.pk).first()
            else:
                existing_user = User.objects.filter(username=username).first()

            if existing_user:
                raise forms.ValidationError("A user with that username already exists, please choose another one")

        return username
