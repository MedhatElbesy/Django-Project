from django.db import models

# Create your models here.

class CategoryStatus(models.TextChoices):
    FAILED = 'Failed'
    SUCCESS = 'Success'
    PENDING = 'Pending'
    UNDER_PROCESS = 'Under Process'
    DELETED = 'Deleted'

class Category(models.Model):
  name=models.CharField(max_length=50, unique=True)
  description=models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, null=True)

  def __str__(self):
    return self.name