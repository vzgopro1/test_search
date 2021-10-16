from django.db import models


class Post231(models.Model):
    title = models.CharField(max_length=100)
    likes = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    views = models.IntegerField()
    photo = models.ImageField(upload_to='Post/')

    def __str__(self):
        return str(self.id)

