from django.db import models
from django.shortcuts import reverse, get_object_or_404

# Create your models here.

class CategoryStatus(models.TextChoices):
    FAILED = 'Failed'
    SUCCESS = 'Success'
    PENDING = 'Pending'
    UNDER_PROCESS = 'Under Process'
    DELETED = 'Deleted'

class Categories(models.Model):
  name=models.CharField(max_length=50, unique=True)
  description=models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, null=True)

  @property
  def show_url(self):
    url = reverse('category_show', args=[self.id])
    return url
  
  @property
  def update_url(self):
    url = reverse('category_update', args=[self.id])
    return url
  
  @property
  def delete_url(self):
    url = reverse('category_delete', args=[self.id])
    return url
  
  @property 
  def get_category_by_id(cls,id):
    return get_object_or_404(cls, pk=id)

  def __str__(self):
    return self.name
