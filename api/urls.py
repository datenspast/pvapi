from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'pv_yield', views.YieldPerKwpViewSet, basename='pv_yield')
urlpatterns = router.urls