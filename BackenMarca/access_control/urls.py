from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from BackenMarca.access_control.access_control import AccessControlView
from BackenMarca.cellar_app.views import CellarViewSet

router = DefaultRouter()
router.register(r'access-control', AccessControlView, basename='access-control')
urlpatterns = router.urls