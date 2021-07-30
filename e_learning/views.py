from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .permissions import IsEducator, IsLearner
from .models import Course, Enrollment
from .serializers import CourseSerializer, CourseEnrollmentSerializer

class HomePageView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:

            if request.user.role == 'learner':
                return render(request,'e_learning/learner_home.html', {})
            elif request.user.role == 'educator':
                return render(request,'e_learning/educator_home.html', {})

        return render(request,'e_learning/home.html', {})


class EducatorCourseView(APIView):
    """docstring for EducatorView. List, update and create courses"""

    permission_classes = [IsAuthenticated,IsEducator]


    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        courses = Course.objects.filter(educator=request.user)
        course_serializer = CourseSerializer(courses, many = True)
        #print(course_serializer.data)
        print(request.user)
        return Response(course_serializer.data)

    def put(self, request, format=None):

        print(request.data)

        try:

            course=self.get_object(request.data['id'])
            course.title=request.data['title']
            if request.data['status'] == 'true':
                course.is_active = True
            else:
                course.is_active = False

            course.save()

            course_serializer = CourseSerializer(course)
            return Response(course_serializer.data)
        except:
            return Response( status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, format=None):

        try:
            print(request.data)
            course = Course()
            course.title = request.data['title']
            if request.data['status'] == 'true':
                course.is_active = True
            else:
                course.is_active = False

            course.educator = request.user
            course.save()
            course_serializer = CourseSerializer(course)
            return Response(course_serializer.data)
        except:
            return Response( status=status.HTTP_400_BAD_REQUEST)



class LearnerEnrollmentView(APIView):

    """Learner will enroll in the courses """

    permission_classes = [IsAuthenticated,IsLearner]


    def get(self, request, format=None):

        courses = Course.objects.filter(is_active = True)
        serializer = CourseEnrollmentSerializer(courses, many=True,context={'request': request})
        return Response(serializer.data)



    def post(self, request, format=None):
        try:
            course = Course.objects.get(id = request.data['course_id'])
            enrollment = Enrollment.objects.create(course = course, learner = request.user)
            serializer = CourseEnrollmentSerializer(course,context={'request': request})
            return Response(serializer.data)
        except:
            return Response( status=status.HTTP_400_BAD_REQUEST)
