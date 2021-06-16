from rest_framework import serializers
from .models import *


class collegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'


class lessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class majorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'


class organizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class teacherSerializer(serializers.ModelSerializer):
    college_id = collegeSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'


class classSerializer(serializers.ModelSerializer):
    major_id = majorSerializer()
    college_id = collegeSerializer()

    class Meta:
        model = Class
        fields = '__all__'


class studentSerializer(serializers.ModelSerializer):
    organization_id = organizationSerializer()
    college_id = collegeSerializer()
    class_id = classSerializer()

    class Meta:
        model = Student
        fields = '__all__'


class selclassSerializer(serializers.ModelSerializer):
    user_id = studentSerializer()
    lesson_id = lessonSerializer()
    class_id = classSerializer()

    class Meta:
        model = Selclass
        fields = '__all__'


class instructSerializer(serializers.ModelSerializer):
    teacher_id = teacherSerializer()
    class_id = classSerializer()
    lesson_id = lessonSerializer()

    class Meta:
        model = Instruct
        fields = '__all__'
