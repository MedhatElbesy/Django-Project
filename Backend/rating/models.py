from django.db import models
from payments.models import Payment, PaymentStatus


class Rating(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]  # Choices from 1 to 5
    rating = models.IntegerField(choices=RATING_CHOICES)
    user = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        'projects.Project', on_delete=models.CASCADE, related_name='ratings'
    )

