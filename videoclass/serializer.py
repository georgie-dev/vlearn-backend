from rest_framework import serializers
from .models import ClassDetails


class ClassSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= ClassDetails
        fields= ['id', 'status', 'lecturer', 'course', 'link']