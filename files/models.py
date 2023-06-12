from django.db import models

# Create your models here.

class CourseMaterials(models.Model):
    course= models.CharField(max_length=100)
    title= models.CharField(max_length=225, unique=True)
    lecturer=models.CharField(max_length=225)
    file= models.FileField(upload_to='course_materials/', null=False, blank=False)
    uploaded_at= models.DateTimeField(auto_now=True)


class UploadAssignment(models.Model):
    course= models.CharField(max_length=100)
    title= models.CharField(max_length=225, unique=True)
    due_date= models.DateTimeField()
    file= models.FileField(upload_to='upload_assignments/', null=False, blank=False)
    lecturer=models.CharField(max_length=225)

class SubmitAssignment(models.Model):
    course= models.CharField(max_length=100)
    title= models.CharField(max_length=225, unique=True)
    submit_date= models.DateTimeField()
    file= models.FileField(upload_to='submitted_assignments/', null=False, blank=False)
    student=models.CharField(max_length=225)

