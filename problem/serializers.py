from rest_framework import serializers
from .models import *
from user.models import User


class problemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'


class ptagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ptag
        fields = '__all__'


class deviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class drecordSerializer(serializers.ModelSerializer):
    device_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Device.objects.all())

    def to_representation(self, instance):
        device = instance.device_id

        data = super(drecordSerializer, self).to_representation(instance)

        data['device_id'] = {
            "id": device.id,
            "name": device.name
        }

        return data

    class Meta:
        model = Drecord
        fields = '__all__'


class pcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pcateory
        fields = '__all__'


class pgroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pgroup
        fields = '__all__'


class poprecordSerializer(serializers.ModelSerializer):
    problem_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Problem.objects.all())
    user_id = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())

    def to_representation(self, instance):
        problem = instance.problem_id
        user = instance.user_id
        data = super(poprecordSerializer, self).to_representation(instance)

        data['probelm_id'] = {
            "id": problem.id,
            "name": problem.name
        }
        data['user_id'] = {
            "id": user.id,
            "name": user.name
        }
        return data

    class Meta:
        model = Poprecord
        fields = '__all__'


class propcateSerializer(serializers.ModelSerializer):
    problem_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Problem.objects.all())
    pcateory_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Pcateory.objects.all())

    def to_representation(self, instance):
        problem = instance.problem_id
        pcateory = instance.pcategory_id
        data = super(propcateSerializer, self).to_representation(instance)

        data['probelm_id'] = {
            "id": problem.id,
            "name": problem.name
        }
        data['pcategory_id'] = {
            "id": pcateory.id,
            "name": pcateory.name
        }
        return data

    class Meta:
        model = Propcate
        fields = '__all__'


class propgroupSerializer(serializers.ModelSerializer):
    pgroup_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Pgroup.objects.all())
    problem_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Problem.objects.all())

    def to_representation(self, instance):
        pgroup = instance.pgroup_id
        problem = instance.problem_id
        data = super(propgroupSerializer, self).to_representation(instance)

        data['pgroup_id'] = {
            "id": pgroup.id,
            "name": pgroup.name
        }
        data['probelm_id'] = {
            "id": problem.id,
            "name": problem.name
        }
        return data

    class Meta:
        model = Propgroup
        fields = '__all__'


class proptagSerializer(serializers.ModelSerializer):
    problem_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Problem.objects.all())
    ptag_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Ptag.objects.all())

    def to_representation(self, instance):
        problem = instance.problem_id
        ptag = instance.ptag_id
        data = super(proptagSerializer, self).to_representation(instance)

        data['ptag_id'] = {
            "id": ptag.id,
            "name": ptag.name
        }
        data['probelm_id'] = {
            "id": problem.id,
            "name": problem.name
        }
        return data

    class Meta:
        model = Proptag
        fields = '__all__'


class psourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psource
        fields = '__all__'


class precordSerializer(serializers.ModelSerializer):
    problem_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Problem.objects.all())
    user_id = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())

    def to_representation(self, instance):
        user = instance.user_id
        problem = instance.problem_id
        data = super(precordSerializer, self).to_representation(instance)

        data['user_id'] = {
            "id": user.id,
            "name": user.name
        }
        data['probelm_id'] = {
            "id": problem.id,
            "name": problem.name
        }
        return data

    class Meta:
        model = Precord
        fields = '__all__'
