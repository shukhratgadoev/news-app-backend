from pyexpat import model
from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title