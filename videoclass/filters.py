import django_filters
from .models import ClassDetails

class ClassFilterSet(django_filters.FilterSet):
    class Meta:
        model= ClassDetails
        fields= ['lecturer', 'course', 'status']