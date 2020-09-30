from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=['id','division','department']

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Major
        fields=['id','major','department_id']

class MajorInSerializer(serializers.ModelSerializer):
    class Meta:
        model=MajorIn
        fields=['major_id','user_id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','code','group','name','department_id']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['id','code','name','classroom','professor_id']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Enrollment
        fields='__all__'
