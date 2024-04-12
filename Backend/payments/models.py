from django.db import models # type: ignore
from accounts.models import User
from projects.views import Project


# Create your models here.
class PaymentStatus(models.TextChoices):
    FAILED = 'Failed'
    SUCCESS = 'Success'
    PENDING = 'Pending'
    UNDER_PROCESS = 'Under Process'
    DELETED = 'Deleted'


class Payment(models.Model):

    project = models.OneToOneField(Project, on_delete=models.CASCADE,null=True, related_name="projectrelated")
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, related_name="accountrelated")
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return f"Payment for {self.project} by {self.user}"
