from django.shortcuts import render
from rest_framework import viewsets, response
from .serializer import CourseMaterialSerializer, UploadAssignmentSerializer
from .models import CourseMaterials, UploadAssignment
from .filters import CourseMaterialsFilter, UploadAssignmentFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class CourseMaterial(viewsets.ModelViewSet):
    queryset = CourseMaterials.objects.all()
    serializer_class = CourseMaterialSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class= CourseMaterialsFilter


class UploadAssignmentView(viewsets.ModelViewSet):
    queryset = UploadAssignment.objects.all()
    serializer_class = UploadAssignmentSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class= UploadAssignmentFilter