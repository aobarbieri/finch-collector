from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=50)
    populationTrend = models.CharField(max_length=50)
    note = models.TextField(max_length=300)

    def __str__(self):
        return self.name