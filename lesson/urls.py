from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = []
router = DefaultRouter()
router.register(r'class', views.classView)
router.register(r'college', views.collegeView)
router.register(r'lesson', views.lessonView)
router.register(r'major', views.majorView)
router.register(r'organization', views.organizationView)
router.register(r'selclass', views.selclassView)
router.register(r'student', views.studentView)
router.register(r'instruct', views.instructView)
router.register(r'teacher', views.teacherView)
urlpatterns += router.urls
