from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
# Create your models here.

class resister(AbstractBaseUser):

    username = models.CharField(max_length=25) 
    email = models.EmailField( unique=True, max_length = 200)  
    date_joined = models.DateTimeField(default=timezone.now)  
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)  
    password  = models.CharField(max_length=10)


