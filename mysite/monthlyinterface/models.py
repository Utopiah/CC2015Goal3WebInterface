import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class Desired_Format(models.Model):
    name = models.CharField(max_length=200, blank=False, default="unset")
    def __str__(self):
        return self.name
    
class Material(models.Model):
    # Should be nearly equivalent to creations but without parents not blends
    desired_format = models.ForeignKey(Desired_Format)
    file_path = models.CharField(max_length=200)
    source_url = models.CharField(max_length=400)
    def __str__(self):
        return self.source_url
    
class Creation(models.Model):
    image_size = models.CharField(max_length=200)
    opacity = models.CharField(max_length=200)
    file_path = models.CharField(max_length=200)
    materials = models.ManyToManyField(Material)
    user = models.ForeignKey(User)
    desired_theme = models.CharField(max_length=200, blank=False, default="unset")
    pub_date = models.DateTimeField('date created')
    desired_format = models.ForeignKey(Desired_Format)
    parent = models.ForeignKey('self', null=True, blank=True)
    def __str__(self):
        return self.desired_theme
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def generate(self):
        #misleading name
        # note that this should NOT be a domain specific application requiring its heavy pip install
            # but... until there are 2 or 3 of those... it better be an existing mess than an empty theoretical perfection
        themes = self.desired_theme
        return dict(themes=themes, image=self.file_path)
    def fork(self):
        from Blend import BlendMe
        result = BlendMe(self.desired_theme)
        themes = self.desired_theme
        return dict(themes=themes, image=self.file_path)
        #return "A blend between all or at least most of the themes " + result + " for the specified format " + '<img src="/'+self.file_path+'">'
