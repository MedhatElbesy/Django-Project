import datetime
from django.db import models
# TODO uncomment the following lines when the models are ready
from accounts.models import User
from categories.models import Category
from tags.models import Tags
from payments.models import Payment

class ProjectStatus(models.TextChoices):
    IN_PROGRESS = 'IP', 'In Progress'
    DONE = 'D', 'Done'


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
        max_length=2, choices=ProjectStatus.choices, default=ProjectStatus.IN_PROGRESS,null=True)
    pictures = models.ImageField(
        upload_to='projects/pictures/')
    video = models.FileField(upload_to='projects/videos/', null=True)
    total_target = models.DecimalField(
        default=0, max_digits=10, decimal_places=2)
    total_collected = models.DecimalField(
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
    def get_remainig_days(self):
        return (self.deadline - datetime.date.today()).days
    @property
    def get_status_display(self):
        return self.status
    @property
    def get_remainig_hours(self):
        return (self.deadline - datetime.date.today()).seconds // 3600
    @property
    def get_progress(self):
        return (self.total_collected / self.total_target) * 100
    @property
    def get_remaining_amount(self):
        if self.total_target > self.total_collected:
            return self.total_target - self.total_collected
        else:
            return 0

    def get_total_payments(self):
        return self.payments.all().count()
    
    def get_project_tags(self):
        return self.tags.all()

    class Meta:
        ordering = ['-created_at']
