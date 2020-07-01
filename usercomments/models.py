from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime 
from django.utils import timezone


class Comment(models.Model):
    
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    hours = models.TimeField(default='0:00 AM')
    comment = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    


    def __str__(self):
        return self.title

    def snippet(self):
        return self.comment[:50]+'...'
