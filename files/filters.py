import django_filters
from .models import CourseMaterials

class CourseMaterialsFilter(django_filters.FilterSet):
    class Meta:
        model= CourseMaterials
        fields= ['lecturer', 'course']