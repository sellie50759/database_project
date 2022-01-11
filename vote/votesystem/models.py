from django.db import models


class VoteSession(models.Model):
    #organizer= models.CharField(max_length=255)  #發起者
    title = models.CharField(max_length=255)
    start_time = models.DateField()
    end_time = models.DateField()
    constraint = models.IntegerField(default=18)
    agree = models.IntegerField()
    disagree = models.IntegerField()
    total = models.IntegerField()
    description = models.CharField(max_length=255)



# Create your models here.
