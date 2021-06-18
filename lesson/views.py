from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .serializers import *
from .models import *
from rest_framework.response import Response


class classView(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = classSerializer

    # def list(self, request, *args, **kwargs):
    #     classList = Class.objects.raw(
    #         "select  * from ego_class,ego_college,ego_major where ego_class.major_id = ego_major.id and ego_class.college_id = ego_college.id")
    #     serializer = self.get_serializer(classList, many=True)
    #     for c in classList and :
    #         print(c.major_id.name)
    #     return Response(serializer.data)

    # def create(self, request):
    #     print(request.data)
    #     return Response(request.data)


class collegeView(ModelViewSet):
    queryset = College.objects.all()
    serializer_class = collegeSerializer


class lessonView(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = lessonSerializer


class majorView(ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = majorSerializer


class organizationView(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = organizationSerializer


class selclassView(ModelViewSet):
    queryset = Selclass.objects.all()
    serializer_class = selclassSerializer


class studentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = studentSerializer


class instructView(ModelViewSet):
    queryset = Instruct.objects.all()
    serializer_class = instructSerializer
