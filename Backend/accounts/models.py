from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import reverse
from uuid import uuid4
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=254, help_text='Required')
    phone_regex = RegexValidator(regex=r'^01[0-2]\d{8}$', message="Phone number must be entered in the format: '01012345678', '01112345678', '01212345678', or '01512345678'.")
    mobile_phone = models.CharField(max_length=11, validators=[phone_regex], unique=True, null=True, blank=True)
    profile_image = models.ImageField(upload_to='accounts/profile_images', null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    facebook_profile = models.URLField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    password_reset_token = models.CharField(max_length=100, blank=True, null=True)
    token_expiration_date = models.DateTimeField(blank=True, null=True)
    is_verified_email = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(null=True, blank=True)
    # google_id = models.CharField(max_length=255, null=True, blank=True)
    # facebook_id = models.CharField(max_length=255, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    

    def __str__(self):
        return self.email

    @property
    def show_url(self):
        pass
        url = reverse('accounts.show', args=[self.id])
        return url

    @property
    def delete_url(self):
        url = reverse('accounts.delete', args=[self.id])
        return url

    @property
    def edit_url(self):
        url = reverse('accounts.edit', args=[self.id])
        return url

    @property
    def image_url(self):
        if self.profile_image:
            return f"/media/{self.profile_image}"
        else:
            return '/media/accounts/profile_images/user.png'

class ActivationKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=32, default=uuid4().hex)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()

    def __str__(self):
        return f'Activation key for {self.user.username}'