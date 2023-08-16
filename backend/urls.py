"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import Users, CoursesList, Login
from files.views import CourseMaterial, UploadAssignmentView, SubmitAssignmentView
from videoclass.views import ClassView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'api/users', Users, basename='users')
router.register(r'api/courses', CoursesList, basename='courses')
router.register(r'api/coursematerials', CourseMaterial, basename='courseMaterials')
router.register(r'api/uploadassignment', UploadAssignmentView, basename='uploadAssignment')
router.register(r'api/submitassignment', SubmitAssignmentView, basename='submitAssignment')
router.register(r'api/class', ClassView.as_view(), name='class-list')


urlpatterns = [
    path('', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)