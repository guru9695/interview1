from django.db import models

# Create your models here.

from django.contrib.auth.models import User

    
class detail(models.Model):
    name= models.ForeignKey(User, on_delete=models.CASCADE,related_name='name')
    usernamedata= models.ManyToManyField(User,related_name='detail')
    
    price = models.CharField(max_length=30, blank=True)
    
    CHOICE= (
        ('owed_by', 'owed_by'),
        ('owes', 'owes'),
    )
    type = models.CharField(max_length=8, choices=CHOICE)
    
