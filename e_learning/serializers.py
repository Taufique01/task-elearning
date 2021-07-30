from rest_framework import serializers
from .models import Course, Enrollment

class CourseSerializer(serializers.ModelSerializer):

    educator = serializers.CharField(source='educator.username')
    class Meta:
        model = Course
        fields = ['id', 'title', 'educator','is_active']



class CourseEnrollmentSerializer(serializers.ModelSerializer):

    educator = serializers.CharField(source='educator.username')
    is_enrolled = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['id', 'title', 'educator','is_enrolled']

    def get_is_enrolled(self, course):
        user =  self.context['request'].user

        try:
            enrollment = Enrollment.objects.get(course = course, learner = user)
            return True
        except Enrollment.DoesNotExist:
            return False
