from django.db import models

# Create your models here.

class CourseMaterials(models.Model):
    course= models.CharField(max_length=100)
    title= models.CharField(max_length=225, unique=True)
    lecturer=models.CharField(max_length=225)
    file= models.FileField(upload_to='course_materials/', null=False, blank=False)
    uploaded_at= models.DateTimeField(auto_now=True)
