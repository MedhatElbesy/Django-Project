from django.db import models 
from django.shortcuts import reverse,get_object_or_404
from django.core.validators import MinValueValidator

# Create your models here.


class PaymentStatus(models.TextChoices):
    FAILED = 'Failed'
    SUCCESS = 'Success'
    PENDING = 'Pending'
    UNDER_PROCESS = 'Under Process'
    DELETED = 'Deleted'


class Payment(models.Model):

    project = models.ForeignKey(
        "projects.Project", on_delete=models.CASCADE, related_name="projectrelated")
    user = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name="accountrelated")
    amount = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    currency = models.CharField(max_length=10)
    status = models.CharField(
        max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f"Payment for {self.project} by {self.user}"

    @property
    def show_url(self):
        url = reverse('paymentsshow',args=[self.id])
        return url
    
    @property 
    def get_payment_by_id(cls,id):
        return get_object_or_404(cls,pk=id)