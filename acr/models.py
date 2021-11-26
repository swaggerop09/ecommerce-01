from django.db import models
from django.db.models.deletion import CASCADE
from login.models import horse

# Create your models here.

class categories(models.Model):
    cname = models.CharField(max_length=10)
    def __str__(self):
        return self.cname

class raw(models.Model):
    cname=models.ForeignKey(categories,on_delete=models.CASCADE,default='')
    name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    des=models.TextField()
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
# class ImageProfile(models.Model):
#     images=models.ImageField(upload_to='images',blank=True)