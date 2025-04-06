from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Status(models.Model):
    name=models.CharField(max_length=128)
    description=models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    static=models.ImageField(upload_to='images/') 
    animated=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=128)
    website=models.URLField(max_length=200)
    description=models.TextField()
    date=models.DateField()
    tags=models.ManyToManyField(Tag, blank=True)
    author=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    status=models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )
    def get_absolute_url(self):
        return reverse("detail", args=[self.id])

    def __str__(self):
        return self.title

