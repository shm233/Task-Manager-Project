from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_User(AbstractUser):
    profile_pic=models.ImageField(upload_to="media/profile_pic",null=True)
    bio = models.TextField()
    
    def __str__(self):
        return self.username

class Task_Model(models.Model):
    PRIORITY = [
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high')
    ]
    STATUS = [
        ('pending','pending'),
        ('in-progress', 'in-progress'),
        ('completed', 'completed')
    ]
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=50, choices=PRIORITY, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS, null=True, blank=True)
    created_by = models.ForeignKey(
        Custom_User,
        on_delete=models.CASCADE,
        null=True,
        related_name='task_creator'
    )
    
    def __str__(self):
        return f'{self.title}'
