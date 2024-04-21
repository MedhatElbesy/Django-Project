import datetime
from django.db import models
from django.db.models import Avg, F, Value
from django.db.models.functions import Coalesce
from multiupload.fields import MultiImageField  # type: ignore

# TODO uncomment the following lines when the models are ready
from accounts.models import User
from categories.models import Category
from tags.models import Tags
from payments.models import Payment, PaymentStatus


class ProjectStatus(models.TextChoices):
    IN_PROGRESS = 'IP', 'In Progress'
    DONE = 'D', 'Done'


def validate_image_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class ProjectImage(models.Model):
    project = models.ForeignKey(
        'Project', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/pictures/')


class Project(models.Model):
    # Attributes definition
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags, related_name='projects')
    ################################################
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=2, choices=ProjectStatus.choices, default=ProjectStatus.IN_PROGRESS, null=True)
    pictures = models.ImageField(
        upload_to='projects/pictures/', validators=[validate_image_extension])

    video = models.FileField(upload_to='projects/videos/', null=True)
    total_target = models.DecimalField(
        default=0, max_digits=10, decimal_places=2)
    total_target = models.DecimalField(
        default=0, max_digits=10, decimal_places=2)
    total_collected = models.DecimalField(
        default=0, max_digits=10, decimal_places=2)
    deadline = models.DateField()
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    # custom functions

    def __str__(self):
        return self.title

    @property
    def get_remaining_days(self):
        return (self.deadline - datetime.date.today()).days

    @property
    def get_status_display(self):
        return self.status

    @property
    def get_remaining_hours(self):
        remaining_time = self.deadline - datetime.date.today()
        remaining_seconds = remaining_time.days * 24 * 3600
        return max(remaining_seconds // 3600, 0)

    @property
    def get_progress(self):
        try:
            # check if total target is not zero
            if self.total_target == 0:
                # throw an err
                raise ZeroDivisionError

            value = (self.total_collected / self.total_target) * 100
            return value
        except ZeroDivisionError:
            return 0

    @property
    def get_remaining_amount(self):
        if self.total_target > self.total_collected:
            return self.total_target - self.total_collected
        else:
            return

    @property
    def get_total_payments(self):
        return self.projectrelated.filter(status__in=[PaymentStatus.SUCCESS, PaymentStatus.PENDING]).count()

    def get_project_rating(self):
        average_rating = self.ratings.aggregate(
            models.Avg('rating'))['rating__avg']
        return average_rating if average_rating is not None else 1

    @property
    def get_total_collected(self):
        return sum(payment.amount for payment in self.projectrelated.all() if payment.status in [PaymentStatus.SUCCESS, PaymentStatus.PENDING])

    @classmethod
    def get_top_five_rated_active_project(cls):
        top_projects = cls.objects.filter(is_active=True).annotate(
            avg_rating=models.Avg('ratings__rating')
        ).order_by('-avg_rating')[:5]
        return top_projects

    @property
    def image_url(self):
        return f"/media/{self.pictures}"

    class Meta:
        ordering = ['-created_at']
