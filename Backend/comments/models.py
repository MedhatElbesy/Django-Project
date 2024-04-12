from django.db import models
from accounts.models import User
from projects.views import Project
from django.core.validators import MinLengthValidator



# Create your models here.
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usercomment")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="projectcomment")
    comment = models.TextField(blank=False , validators=[MinLengthValidator(4)])
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)