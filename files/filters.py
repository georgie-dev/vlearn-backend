import django_filters
from .models import CourseMaterials, UploadAssignment, SubmitAssignment

class CourseMaterialsFilter(django_filters.FilterSet):
    class Meta:
        model= CourseMaterials
        fields= ['lecturer', 'course']

class UploadAssignmentFilter(django_filters.FilterSet):
    class Meta:
        model= UploadAssignment
        fields= ['lecturer', 'course']

class SubmitAssignmentFilter(django_filters.FilterSet):
    class Meta:
        model= SubmitAssignment
        fields= ['student', 'course']