from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=50)
    populationTrend = models.CharField(max_length=50)
    note = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    # The create and edit classs functions will use this to redirect after the process is complete
    # kwargs is optional but in this case is necessary because we are using an id
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})