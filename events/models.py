from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=40)
    desc = RichTextField()
    date = models.DateField()
    time = models.CharField(max_length=10)
    eventDuration = models.CharField(max_length=10)
    location = models.CharField(max_length=40)
    slug = models.SlugField(default="", null=False, unique=True, db_index=True)
    category = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.name}"