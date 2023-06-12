from rest_framework import serializers
from .models import CourseMaterials, UploadAssignment, SubmitAssignment


class CourseMaterialSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=CourseMaterials
        fields= ['id', 'course', 'title', 'lecturer', 'file', 'uploaded_at']

class UploadAssignmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model= UploadAssignment
        fields= ['id', 'course', 'title', 'lecturer', 'due_date', 'file']

class SubmitAssignmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model= SubmitAssignment
        fields= ['id', 'course', 'title', 'student', 'submit_date', 'file']
