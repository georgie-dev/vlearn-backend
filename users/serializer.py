from rest_framework import serializers
from django.conf import settings
from .models import Courses, User


class CourseSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
      model=Courses
      fields=['id', 'courseCode', 'courseStatus', 'courseTitle', 'courseUnit','level', 'semester', 'department']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields=['id','firstname', 'lastname', 'email', 'faculty', 'level', 'department', 'matricNo', 'password', 'imageUrl']

        extra_kwargs = {"password": {"write_only": True}}


    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
