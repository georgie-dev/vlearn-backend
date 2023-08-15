from django.db import models

# Create your models here.
class ClassDetails(models.Model):
    lecturer = models.CharField(max_length=225)
    course = models.CharField(max_length=225)
    link = models.CharField(max_length=225)
    status= models.CharField(default='Live', max_length=225)