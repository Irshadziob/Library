from django.db import models


# Create your models here.
class Library(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallery')
    author = models.CharField(max_length=250);
    descreption = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return self.name



