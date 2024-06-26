from django.db import models
 
# Create your models here.

class Quiz(models.Model):
    course =models.CharField(max_length=225)
    duration=models.PositiveIntegerField()
    assessment_date= models.DateTimeField()
    total_marks= models.IntegerField()
    instructions= models.TextField()


class QuesModel(models.Model):
    quiz= models.ForeignKey (Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    options = models.JSONField()
    correct_option = models.PositiveIntegerField()
    
    def __str__(self):
        return self.question
    