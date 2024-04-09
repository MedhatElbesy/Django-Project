from django.db import models
from django.shortcuts import reverse,get_object_or_404
# from accounts.models import user
# from projects.models import project




# Create your models here.
class Payment(models.Model):
    # project = models.OneToOneField(project,on_delete=models.CASCADE,related_name="projectrelated")
    # user = models.OneToOneField(user,on_delete=models.CASCADE,related_name="accountrelated")
    amount = models.IntegerField()
    currency = models.CharField(max_length=10)
    status = models.CharField()


    @property
    def show_url(self):
        url = reverse('booksshow',args=[self.id])
        return url
    
        
    @property
    def get_book_by_id(cls,id):
        return get_object_or_404(cls,pk=id)