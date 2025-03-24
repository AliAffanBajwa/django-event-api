from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    priority = models.IntegerField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)

    def __str__(self):
        return self.name
