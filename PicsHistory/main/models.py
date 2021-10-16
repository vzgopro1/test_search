from django.db import models

class HistoryGenere(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class HistoryWords(models.Model):
    sentenceAuthor = models.CharField(max_length=20)
    place = models.IntegerField()
    sentence = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

class History(models.Model):
    title = models.CharField(max_length=30)
    genre = models.ForeignKey(HistoryGenere, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='HistoryMedia')
    words = models.ManyToManyField(HistoryWords)