from django.db import models

class PublicationLikes(models.Model):
    likeAuthor = models.IntegerField()

class Publication(models.Model):
    title = models.CharField(max_length=25)
    views = models.IntegerField()
    likes = models.