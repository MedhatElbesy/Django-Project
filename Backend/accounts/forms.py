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
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'mobile_phone', 'profile_image')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['first_name'] + '_' + self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, max_length=254, help_text='Required',
                             widget=forms.EmailInput(attrs={"autocomplete": "email"}))
    first_name = forms.CharField(required=True, max_length=150, validators=[MinLengthValidator(2)])
    last_name = forms.CharField(required=True, max_length=150, validators=[MinLengthValidator(2)])
    is_superuser = forms.BooleanField(label='Is Superuser', required=False, widget=forms.RadioSelect(choices=((True, '1'), (False, '0'))))
    is_staff = forms.BooleanField(label='Is Staff', required=False, widget=forms.RadioSelect(choices=((True, '1'), (False, '0'))))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'mobile_phone', 'profile_image', 'is_superuser', 'is_staff')

    def clean_email(self):
        email = self.cleaned_data['email']
        email_found = User.objects.filter(email=email).exists()
        if email_found:
            instance = getattr(self, 'instance', None)
            if instance and instance.pk:
                existing_user = User.objects.filter(email=email).exclude(pk=instance.pk).first()
            else:
                existing_user = User.objects.filter(email=email).first()

            if existing_user:
                raise forms.ValidationError('Email address is already used, please choose another one')

        return email

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if username:
    #         # Retrieve the current user instance from the form's instance attribute
    #         instance = getattr(self, 'instance', None)
    #         if instance and instance.pk:
    #             # Exclude the current user from the uniqueness check
    #             existing_user = User.objects.filter(username=username).exclude(pk=instance.pk).first()
    #         else:
    #             existing_user = User.objects.filter(username=username).first()
    #
    #         if existing_user:
    #             raise forms.ValidationError("A user with that username already exists, please choose another one")
    #
    #     return username
