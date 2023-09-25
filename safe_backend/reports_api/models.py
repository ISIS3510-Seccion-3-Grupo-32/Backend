from django.db import models
from user_api.models import AppUser

class Report(models.Model):

    username = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='reporting_user')
    report = models.CharField(max_length=100)
    direction = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date_time = models.DateTimeField()

    def __str__(self):
        self.report
