from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    uploaded_time = models.DateTimeField(auto_now=True)


class Podcast(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    uploaded_time = models.DateTimeField(auto_now=True)
    host = models.CharField(max_length=100)
    participents = models.JSONField(null=True,blank=True)

    

class Audiobook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.IntegerField()
    uploaded_time = models.DateTimeField(auto_now=True)


    
