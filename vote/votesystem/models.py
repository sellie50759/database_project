from django.db import models
from django.contrib.auth.models import User


class VoteSession(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)  #發起者
    title = models.CharField(max_length=255)
    start_time = models.DateField()
    end_time = models.DateField()
    # constraint = models.IntegerField(default=18)
    agree = models.IntegerField(default=0)
    disagree = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    description = models.CharField(max_length=255)


class VoteRecord(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)  # 發起者
    session = models.ForeignKey(VoteSession, on_delete=models.CASCADE)
    is_agree = models.BooleanField()

# Create your models here.
