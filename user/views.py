from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import *
from .models import User, Role
from .utils import isAdmin
from django.contrib.auth import authenticate
import os


# 注册登录相关
class UserProfileView(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk):
        user = User.objects.get(pk=pk)
        role = Role.objects.filter(user_id=pk)
        roles = []
        for r in role:
            roles.append(r.name)

        serializer = UserSerializer(user)
        data = serializer.data
        data['roles'] = roles
        return Response(data)

    @action(methods=['post'], detail=False)
    def exist(self, request):
        username = request.data['username']
        count = User.objects.filter(username=username).count()
        data = {
            "username": username,
            "count": count
        }
        return Response(data)

    @action(methods=['put'], detail=False)
    def changePassword(self, request):
        data = request.data
        user = request.user
        credentials = {
            'username': user.username,
            'password': data['oldpassword']
        }
        if authenticate(**credentials):
            newpassword = {
                'password': data['newpassword']
            }
            UserSerializer.changePassword(self, newpassword, request)
            return Response({"status": 1})

        return Response({"status": 0})

    @action(methods=['post'], detail=True)
    def avatar(self, request, pk):
        avatar = request.data['file']
        # print(avatar)
        avatar.name = pk + '.png'
        os.remove('avatar/' + avatar.name)
        user = User.objects.get(pk=pk)
        user.avatar = avatar
        user.save()
        return Response({"status": 200})


class UserView(ModelViewSet):
    # permission_classes = (isAdmin,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['post'], detail=False)
    def add(self, request):
        data = request.data
        data['password'] = "123456"
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def unchecked(self, request):
        userList = User.objects.filter(status="FALSE")
        serializer = UserSerializer(userList, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def check(self, request):
        data = request.data
        for user in data:
            User.objects.filter(id=user['id']).update(status=user['status'])
        return Response(data)


class RoleView(ModelViewSet):
    permission_classes = (isAdmin,)
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    @action(methods=['post'], detail=False)
    def assign(self, request):
        data = request.data
        print(data)
        user = User.objects.get(id=data['id'])
        role = {'role_id': 1, 'name': 'admin', 'user': user.id}
        serializer = self.get_serializer(data=role, context={'request': self.request})
        serializer.is_valid()
        serializer.save()

        # Role.objects.create(role_id=1, name='admin', assign_id=request.user.id, user_id=user.id)
        # # print(serializer.data)
        return Response(status=200)

    @action(methods=['get'], detail=False)
    def unadmin(self, request):
        user = User.objects.raw(
            "select * from ego_user where id NOT IN(select user_id from ego_role where name = 'admin')")
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def admin(self, request):
        user = User.objects.raw("select *,eu.name from ego_role left join ego_user eu on ego_role.USER_ID = eu.ID")
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
