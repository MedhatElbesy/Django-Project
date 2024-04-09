from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^01[0-2]\d{8}$', message="Phone number must be entered in the format: '01012345678', '01112345678', '01212345678', or '01512345678'.")
    mobile_phone = models.CharField(max_length=11, validators=[phone_regex], unique=True, null=True, blank=True)
    profile_image = models.ImageField(upload_to='accounts/profile_images', null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    facebook_profile = models.URLField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(null=True, blank=True)
    # google_id = models.CharField(max_length=255, null=True, blank=True)
    # facebook_id = models.CharField(max_length=255, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'password']
