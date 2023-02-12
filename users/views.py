from django.contrib.auth.hashers import check_password
from .models import Courses, User
from .serializer import CourseSerializer, UserSerializer
from .filters import UserFilterSet, CoursesFilterSet
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import login
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt




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

    def create(self, request, *args, **kwargs):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                account = serializer.save()
                account.is_active = True
                account.save()
                token = Token.objects.get_or_create(user=account)[0].key
                data = {}
                data["matricNo"] = account.matricNo
                data["level"] = account.level
                data["department"] = account.department
                data["faculty"] = account.faculty
                data["id"] = account.id
                return Response(data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'firstname': user.firstname,
            'email': user.email,
            'matric_no': user.matricNo,
            'faculty': user.faculty,
            'level': user.level,
            'department': user.department,
            'is_staff': user.is_staff,
            'lastname': user.lastname,
            'imageUrl': user.imageUrl,
            # 'courses': user.courses,
        })
