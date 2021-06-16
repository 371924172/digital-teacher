from rest_framework import serializers
from .models import *
from user.serializers import UserSerializer

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
    device_id = deviceSerializer()

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
    problem_id = problemSerializer()
    user_id = UserSerializer()
    class Meta:
        model = Poprecord
        fields = '__all__'


class propcateSerializer(serializers.ModelSerializer):
    problem_id = problemSerializer()
    pcateory_id = pcategorySerializer()
    class Meta:
        model = Propcate
        fields = '__all__'


class propgroupSerializer(serializers.ModelSerializer):
    pgroup_id = pgroupSerializer()
    problem_id = problemSerializer()
    class Meta:
        model = Propgroup
        fields = '__all__'


class proptagSerializer(serializers.ModelSerializer):
    problem_id = problemSerializer()
    ptag_id = ptagSerializer()
    class Meta:
        model = Proptag
        fields = '__all__'


class psourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psource
        fields = '__all__'

class precordSerializer(serializers.ModelSerializer):
    problem_id = problemSerializer()
    user_id = UserSerializer()
    class Meta:
        model = Precord
        fields = '__all__'