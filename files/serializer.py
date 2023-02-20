from rest_framework import serializers
from .models import CourseMaterials


class CourseMaterialSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=CourseMaterials
        fields= ['course', 'title']