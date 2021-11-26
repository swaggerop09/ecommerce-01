from django.db import models

# Create your models here.
class horse(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=20)
    phn=models.PositiveIntegerField()
    mail=models.EmailField()
    Male = '1'
    Female = '2'
    Gender = [
        (Male,'MALE'),
        (Female,'FEMALE')
    ]
    gender=models.CharField(max_length=2,choices=Gender)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.username
