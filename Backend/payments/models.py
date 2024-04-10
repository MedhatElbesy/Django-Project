from django.db import models
from accounts.models import User
from projects.views import Project


# Create your models here.
class Payment(models.Model):
    project = models.OneToOneField(
        Project, on_delete=models.CASCADE, related_name="projectrelated")
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="accountrelated")
    amount = models.IntegerField()
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Payment for {self.roject} by {self.user}"
