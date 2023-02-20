from django.db import models

# Create your models here.

class CourseMaterials(models.Model):
    course= models.CharField(max_length=100)
    title= models.CharField(max_length=225)
    lecturer=models.CharField(max_length=225)
    file_name= models.CharField(max_length=225)
