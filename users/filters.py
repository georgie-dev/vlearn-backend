import django_filters
from .models import User, Courses

class StudentFilterSet(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['matricNo']

class CoursesFilterSet(django_filters.FilterSet):
    class Meta:
        model = Courses
        fields= ['department', 'level', 'semester']