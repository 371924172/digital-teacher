from rest_framework import serializers
from .models import *
from user.models import User


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
    college_id = serializers.PrimaryKeyRelatedField(many=False, queryset=College.objects.all())

    def to_representation(self, instance):
        college = instance.college_id
        data = super(teacherSerializer, self).to_representation(instance)
        data["college_id"] = {
            "id": college.id,
            "name": college.name
        }

        return data

    class Meta:
        model = Teacher
        fields = '__all__'


class classSerializer(serializers.ModelSerializer):
    # major_id = majorSerializer()
    # college_id = collegeSerializer()

    major_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Major.objects.all())
    college_id = serializers.PrimaryKeyRelatedField(many=False, queryset=College.objects.all())

    def to_representation(self, instance):
        major = instance.major_id
        college = instance.college_id
        data = super(classSerializer, self).to_representation(instance)
        data['major_id'] = {
            "id": major.id,
            "name": major.name
        }
        data["college_id"] = {
            "id": college.id,
            "name": college.name
        }

        return data

    class Meta:
        model = Class
        fields = '__all__'

    # def validate(self, attrs):
    #     attrs['major_id'] = Major.objects.get
    #     return attrs


class studentSerializer(serializers.ModelSerializer):
    organization_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Organization.objects.all())
    college_id = serializers.PrimaryKeyRelatedField(many=False, queryset=College.objects.all())
    class_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Class.objects.all())

    def to_representation(self, instance):
        organization = instance.organization_id
        college = instance.college_id
        c = instance.class_id

        data = super(studentSerializer, self).to_representation(instance)
        data['organizationid'] = {
            "id": organization.id,
            "name": organization.name
        }
        data["college_id"] = {
            "id": college.id,
            "name": college.name
        }
        data['class_id'] = {
            "id": c.id,
            "name": c.name
        }

        return data

    class Meta:
        model = Student
        fields = '__all__'


class selclassSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())
    lesson_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Lesson.objects.all())
    class_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Class.objects.all())

    def to_representation(self, instance):
        user = instance.user_id
        lesson = instance.lesson_id
        c = instance.class_id

        data = super(selclassSerializer, self).to_representation(instance)
        data['user_id'] = {
            "id": user.id,
            "name": user.name
        }
        data["lesson_id"] = {
            "id": lesson.id,
            "name": lesson.name
        }
        data['class_id'] = {
            "id": c.id,
            "name": c.name
        }

        return data

    class Meta:
        model = Selclass
        fields = '__all__'


class instructSerializer(serializers.ModelSerializer):
    teacher_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Teacher.objects.all())
    class_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Class.objects.all())
    lesson_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Lesson.objects.all())

    def to_representation(self, instance):
        teacher = instance.teacher_id
        lesson = instance.lesson_id
        c = instance.class_id

        data = super(instructSerializer, self).to_representation(instance)
        data['teacher_id'] = {
            "id": teacher.id,
            "name": teacher.name
        }
        data["lesson_id"] = {
            "id": lesson.id,
            "name": lesson.name
        }
        data['class_id'] = {
            "id": c.id,
            "name": c.name
        }

        return data

    class Meta:
        model = Instruct
        fields = '__all__'
