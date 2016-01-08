import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Desired_Format(models.Model):
    name = models.CharField(max_length=200, blank=False, default="unset")
    def __str__(self):
        return self.name
    
class Creation(models.Model):
    desired_theme = models.CharField(max_length=200, blank=False, default="unset")
    pub_date = models.DateTimeField('date created')
    desired_format = models.ForeignKey(Desired_Format)
    parent = models.ForeignKey('self', null=True, blank=True)
    def __str__(self):
        return self.desired_theme
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def generate(self):
        return "A blend between all or at least most of the themes " + self.desired_theme + " for the specified format "
        # fails for implicit to str " for the specified format (" + self.desired_format + ")"

        #import BlendMeAPicture
        # problem between Python2 and Python3...
        #cheating until it (month1) becomes a library compatible to python3
        # https://github.com/Utopiah/CC2015Goal3Month1/blob/master/BlendMeAPicture.py
