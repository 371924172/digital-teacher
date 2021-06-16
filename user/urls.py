from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^authenticated/$', obtain_jwt_token),
    url(r'^changePassword/', views.UserProfileView.as_view({'put': 'changePassword'})),
    url(r'^updateIssuperuser/', views.UserView.as_view({'put': 'updateIssuperuser'})),
]

router = DefaultRouter()
router.register(r'users', views.UserView)
router.register(r'userProfile', views.UserProfileView)
router.register(r'role', views.RoleView)
urlpatterns += router.urls
