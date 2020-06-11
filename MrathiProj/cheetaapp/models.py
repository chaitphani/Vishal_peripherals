from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    location = models.CharField(max_length=120, null=True, blank=True)
    experience = models.CharField(max_length=120, null=True, blank=True)
    qualification = models.CharField(max_length=120, null=True, blank=True)
    salary = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='cards', null=True, blank=True)

    def __str__(self):
        return self.title