from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CourseMaterialSerializer
from .models import CourseMaterials

# Create your views here.

class CourseMaterial(viewsets.ModelViewSet):
    queryset = CourseMaterials.objects.all()
    serializer_class = CourseMaterialSerializer