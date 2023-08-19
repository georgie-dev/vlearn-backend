import django_filters
from .models import Quiz

class QuizFilterSet(django_filters.FilterSet):
    model = Quiz
    fields = ['course']