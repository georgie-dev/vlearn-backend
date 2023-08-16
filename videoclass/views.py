from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ClassSerializers
from .filters import ClassFilterSet
from .models import ClassDetails
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class ClassListView(APIView):
    def get(self, request, *args, **kwargs):
        course_codes = request.GET.get('course', '')  # Get the 'course' parameter
        
        if course_codes:
            course_code_list = course_codes.split(',')  # Split comma-separated values
            # Now you have the list of course codes, use it for filtering
            classes = ClassDetails.objects.filter(course__in=course_code_list)
        else:
            classes = ClassDetails.objects.all()
        
        # Serialize the classes and return the response
        serialized_classes = ClassSerializers(classes, many=True)
        return Response(serialized_classes.data)