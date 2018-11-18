from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    type = models.CharField(max_length=20,default='')
    name = models.CharField(max_length=40,default='')
    mobile = models.CharField(max_length=12,default='')
    address = models.TextField(max_length=None,default='')
    bloodgroup1 = models.CharField(max_length=4,default='',blank=True)
    bloodgroup2 = models.CharField(max_length=4,default='',blank=True)
    bloodgroup3 = models.CharField(max_length=4,default='',blank=True)
    bloodgroup4 = models.CharField(max_length=4,default='',blank=True)
    bloodgroup5 = models.CharField(max_length=4,default='',blank=True)
    bloodgroup6 = models.CharField(max_length=4,default='',blank=True)
    bloodgroup7 = models.CharField(max_length=4,default='',blank=True)
    bloodgroup8 = models.CharField(max_length=4,default='',blank=True)

    def __str__(self):
        return self.name
