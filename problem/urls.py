from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = []

router = DefaultRouter()
router.register(r'problem', views.problemView)
router.register(r'ptag', views.ptagView)
router.register(r'device', views.deviceView)
router.register(r'drecord', views.drecordView)
router.register(r'pcategory', views.pcategoryView)
router.register(r'pgroup', views.pgroupView)
router.register(r'poprecord', views.poprecordView)
router.register(r'propcate', views.propcateView)
router.register(r'propgroup', views.propgroupView)
router.register(r'proptag', views.proptagView)
router.register(r'psource', views.psourceView)
urlpatterns += router.urls
