from django.db import models

class ServicesCategory(models.Model):
    name = models.CharField(max_length=60)

class Services(models.Model):

    price = models.IntegerField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name