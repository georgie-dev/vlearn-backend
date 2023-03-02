import django_filters
from .models import CourseMaterials, UploadAssignment

class CourseMaterialsFilter(django_filters.FilterSet):
    class Meta:
        model= CourseMaterials
        fields= ['lecturer', 'course']

class UploadAssignmentFilter(django_filters.FilterSet):
    class Meta:
        model= UploadAssignment
        fields= ['lecturer', 'course']