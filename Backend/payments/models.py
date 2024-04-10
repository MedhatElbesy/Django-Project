from django.db import models
from django.shortcuts import reverse,get_object_or_404
# from accounts.models import user
# from projects.models import project

# Create your models here.
class PaymentStatus(models.TextChoices):
    FAILED = 'Failed'
    SUCCESS = 'Success'
    PENDING = 'Pending'
    UNDER_PROCESS = 'Under Process'
    DELETED = 'Deleted'

class Payment(models.Model):
    # project = models.OneToOneField(project,on_delete=models.CASCADE,related_name="projectrelated")
    # user = models.OneToOneField(user,on_delete=models.CASCADE,related_name="accountrelated")
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    @property
    def show_url(self):
        url = reverse('booksshow',args=[self.id])
        return url
    
        
    @property
    def get_book_by_id(cls,id):
        return get_object_or_404(cls,pk=id)