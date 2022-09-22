from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title
    