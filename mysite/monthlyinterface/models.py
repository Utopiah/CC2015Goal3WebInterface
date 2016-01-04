import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Desired_Format(models.Model):
    name = models.CharField(max_length=200, blank=False, default="unset")
    
class Creation(models.Model):
    desired_theme = models.CharField(max_length=200, blank=False, default="unset")
    pub_date = models.DateTimeField('date created')
    desired_format = models.ForeignKey(Desired_Format)
    parent = models.ForeignKey('self', null=True, blank=True)
    def __str__(self):
        return self.desired_theme
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
