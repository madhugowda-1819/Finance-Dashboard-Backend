from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('viewer', 'Viewer'),
        ('analyst', 'Analyst'),
        ('admin', 'Admin'),
    )
     
    role=models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
