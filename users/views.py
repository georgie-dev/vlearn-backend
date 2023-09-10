from .models import Courses, User
from .serializer import CourseSerializer, UserSerializer
from .filters import UserFilterSet, CoursesFilterSet
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()



class CoursesList(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class= CoursesFilterSet

    def patch(self, request, pk):
        instance = self.get_object(pk)
        if not instance:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Users(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class= UserFilterSet



    def patch(self, request, pk):
        instance = self.get_object(pk)
        if not instance:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
            'token': token.key,
            'user_id': user.pk,
            'title': user.title,
            'firstname': user.first_name,
            'lastname': user.last_name,
            'email': user.email,
            'matric_no': user.matricNo,
            'faculty': user.faculty,
            'level': user.level,
            'department': user.department,
            'is_staff': user.is_staff,
            'imageUrl': user.imageUrl,
            'is_staff': user.is_staff,
            'courses': user.courses.values(),
            })
        return Response('Account Does not exist')
