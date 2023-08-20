from rest_framework import serializers
from .models import Quiz, QuesModel

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuesModel
        fields = '__all__'  

        extra_kwargs = {"correct_option": {"write_only": True}}

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = '__all__'  
