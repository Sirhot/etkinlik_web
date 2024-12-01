from django.db import models
from account.models import CustomUser
from django.utils.text import slugify

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=40)
    desc = models.TextField()
    date = models.DateField()
    time = models.CharField(max_length=10)
    eventDuration = models.CharField(max_length=10)
    location = models.CharField(max_length=40)
    slug = models.SlugField(default="", null=False, unique=True, db_index=True)
    isActive = models.BooleanField(default=False)
    category = models.CharField(max_length=40)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(args,kwargs)
    
    def __str__(self):
        return f"{self.name}"

class Participant(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="participations")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="participants")
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"
    
    class Meta:
        unique_together = ("user", "event")