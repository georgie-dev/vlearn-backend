from django.shortcuts import render
from rest_framework import viewsets, status
from .serializer import ClassSerializers
from .models import ClassDetails
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class ClassListView(viewsets.ModelViewSet):
    queryset = ClassDetails.objects.all()
    serializer_class = ClassSerializers

    @action(detail=False, methods=['GET'])
    def filter_by_course(self, request):
        course_codes = self.request.query_params.get('course', '')
        
        if course_codes:
            course_code_list = course_codes.split(',')
            classes = self.queryset.filter(course__in=course_code_list)
            serialized_classes = self.serializer_class(classes, many=True)
            return Response(serialized_classes.data)
        else:
            return Response("No course codes provided", status=status.HTTP_400_BAD_REQUEST)