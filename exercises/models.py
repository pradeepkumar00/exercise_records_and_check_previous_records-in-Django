from django.db import models

# Create your models here.
class exer(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    wt = models.CharField(max_length=50)
    energy = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    mm = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    def __str__(self):
        return self.name