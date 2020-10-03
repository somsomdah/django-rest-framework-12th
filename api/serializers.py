from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Major
        fields='__all__'

class MajorInSerializer(serializers.ModelSerializer):
    class Meta:
        model=MajorIn
        fields='__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['id','code','group','name','department_id']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['id','code','name','classroom','professor_id']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Enrollment
        fields='__all__'
