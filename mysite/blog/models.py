from django.db import models

# Create your models here.
from django.db import models
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)