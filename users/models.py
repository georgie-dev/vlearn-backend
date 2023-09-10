from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.

class Courses(models.Model):
    courseCode= models.CharField(max_length=10, unique=True)
    courseStatus= models.CharField(max_length=2)
    courseTitle=models.CharField(max_length=100)
    courseUnit= models.IntegerField()
    semester= models.CharField(max_length=100)
    level=models.CharField(max_length=100)
    department=models.CharField(max_length=100)


class CustomUserManager(UserManager):

    def create_user(self, matricNo, password, **extra_fields):

        if not matricNo:
            raise ValueError("The matricNo must be set")
        user = self.model(
            matric_no=self.matricNo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user



class User(AbstractUser):
    username= None
    title=models.CharField(max_length= 15, null=True)
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    faculty = models.CharField(max_length=100)
    level= models.CharField(max_length=100)
    department =models.CharField(max_length=100)
    matricNo = models.CharField(max_length=100, unique=True) 
    password = models.CharField(max_length=100)
    imageUrl= models.CharField(max_length=100, null=True)
    courses= models.ManyToManyField(Courses, blank=True)
    date_joined = models.DateField(max_length=100, auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "matricNo"
    REQUIRED_FIELDS = []

    objects=CustomUserManager()

    def __str__(self):
        return str(self.matricNo)


