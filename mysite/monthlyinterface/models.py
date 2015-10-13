from django.db import models

# Create your models here.

class Creation(models.Model):
    desire_theme = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date created')
