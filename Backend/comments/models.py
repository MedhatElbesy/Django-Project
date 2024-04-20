from django.db import models
from django.core.validators import MinLengthValidator
from accounts.models import User
from projects.models import Project


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments")  # Use the User model directly
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="project_comments")  # Use the Project model directly
    comment = models.TextField(blank=False, validators=[MinLengthValidator(4)])
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = (("user", "project"),)
