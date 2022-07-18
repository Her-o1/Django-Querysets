from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from . import managers

# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length = 200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_Date = models.DateTimeField(default=datetime.now, blank=True)
    active = models.BooleanField(default=True)
    objects = models.Manager()
    public = managers.ActiveLinkManager()

    def __str__(self):
        return self.description

