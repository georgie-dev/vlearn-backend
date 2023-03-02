from rest_framework import serializers
from .models import CourseMaterials, UploadAssignment


class CourseMaterialSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=CourseMaterials
        fields= ['id', 'course', 'title', 'lecturer', 'file', 'uploaded_at']

class UploadAssignmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model= UploadAssignment
        fields= ['id', 'course', 'title', 'lecturer', 'due_date', 'file']
