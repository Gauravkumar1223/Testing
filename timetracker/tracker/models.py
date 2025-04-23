# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class CustomUser(AbstractUser):
    position = models.CharField(max_length=100, blank=True)
    team_lead = models.CharField(max_length=100, blank=True)
    project_manager = models.CharField(max_length=100, blank=True)
    project = models.CharField(max_length=100, blank=True)
    vacation_days = models.PositiveIntegerField(default=20)
    vacation_days_old = models.PositiveIntegerField(default=10)
    signature = models.BinaryField(null=True, blank=True)


    def __str__(self):
        return self.username


class TimeEntry(models.Model):
    DAY_TYPE_CHOICES = [
        ('work', 'Working Day'),
        ('holiday', 'Holiday'),
        ('sick', 'Sick Day'),
        ('vacation', 'Vacation'),
    ]  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)  # You can remove null=True when implementing user authentication
    date = models.DateField()
    hours = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    day_type = models.CharField(max_length=10, choices=DAY_TYPE_CHOICES, default='work')
    
    class Meta:
        # Ensure one entry per date per user
        unique_together = ['user', 'date']
