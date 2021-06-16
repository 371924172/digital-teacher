from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class problemView(ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = problemSerializer

    def create(self, request):
        data = request.data
        last = Problem.objects.last()
        data['problem_id'] = 'P' + str((int(last.problem_id[1:]) + 1)).zfill(5)
        serializer = self.get_serializer(data=data)
        serializer.is_valid()
        serializer.save()
        return Response(request.data)

    @action(methods=['get'], detail=False)
    def myProblem(self, request):
        MyProblemList = Problem.objects.filter(created_by=request.user.id)
        serializer = problemSerializer(MyProblemList, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def publishCheck(self):
        # publishCheckList = Problem.objects.filter(publish_status_in=[0, 1, 2, 3])

        serializer = problemSerializer(publishCheckList, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def publishAccept(self, request):
        id = request.data['id']
        problem = Problem.objects.get(id=id)
        problem.publish_status = 2
        problem.save()
        return Response({"status": 200})

    @action(methods=['post'], detail=False)
    def publishReject(self, request):
        id = request.data['id']
        problem = Problem.objects.get(id=id)
        problem.publish_status = 3
        problem.save()
        return Response({"status": 200})


class ptagView(ModelViewSet):
    queryset = Ptag.objects.all()
    serializer_class = ptagSerializer


class deviceView(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = deviceSerializer


class drecordView(ModelViewSet):
    queryset = Drecord.objects.all()
    serializer_class = drecordSerializer


class pcategoryView(ModelViewSet):
    queryset = Pcateory.objects.all()
    serializer_class = pcategorySerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(request.data)


class pgroupView(ModelViewSet):
    queryset = Pgroup.objects.all()
    serializer_class = pgroupSerializer

    def create(self, request):
        data = request.data
        count = Pgroup.objects.filter(name=data['name']).count()
        if count:
            return Response({"code": 0, "message": "题单名称重复"})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def myPgroup(self, request):
        user = request.user
        pgroupList = Pgroup.objects.filter(create_by=user.id)
        serializer = pgroupSerializer(pgroupList)
        return Response(serializer.data)


class poprecordView(ModelViewSet):
    queryset = Poprecord.objects.all()
    serializer_class = poprecordSerializer


class propcateView(ModelViewSet):
    queryset = Poprecord.objects.all()
    serializer_class = poprecordSerializer


class propgroupView(ModelViewSet):
    queryset = Propgroup.objects.all()
    serializer_class = propgroupSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        print(data)
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data)

    @action(methods=['post'], detail=False)
    def listOfId(self, request):
        data = request.data
        ProblemList = Problem.objects.raw(
            "select * from ego_propgroup left join ego_problem on ego_propgroup.problem_id = ego_problem.id where ego_propgroup.pgroup_id = %s",
            [data['id']])
        serializer = problemSerializer(ProblemList, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=False)
    def outofPgroup(self, request):
        data = request.data
        print(data)
        ProblemList = Problem.objects.raw(
            "select * from ego_problem where id not in (select problem_id from ego_propgroup where pgroup_id = %s)",
            [data['id']])
        serializer = problemSerializer(ProblemList, many=True)
        return Response(serializer.data)

    @action(methods=['delete'], detail=False)
    def batchDelete(self, request):
        data = request.data
        print(data)
        for d in data:
            propgroup = Propgroup.objects.get(id=d['id'])
            propgroup.delete()
        return Response(status=status.HTTP_200_OK)


class proptagView(ModelViewSet):
    queryset = Proptag.objects.all()
    serializer_class = proptagSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(request.data)


class psourceView(ModelViewSet):
    queryset = Psource.objects.all()
    serializer_class = psourceSerializer
