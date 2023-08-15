from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ClassSerializers
from .filters import ClassFilterSet
from .models import ClassDetails
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ClassView(viewsets.ModelViewSet):
    queryset = ClassDetails.objects.all()
    serializer_class= ClassSerializers
    filter_backends= [DjangoFilterBackend]
    filterset_class = ClassFilterSet