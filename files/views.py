from django.shortcuts import render
from rest_framework import viewsets, response
from .serializer import CourseMaterialSerializer
from .models import CourseMaterials
from .filters import CourseMaterialsFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class CourseMaterial(viewsets.ModelViewSet):
    queryset = CourseMaterials.objects.all()
    serializer_class = CourseMaterialSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class= CourseMaterialsFilter
