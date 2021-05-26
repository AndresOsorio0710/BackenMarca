from rest_framework.routers import DefaultRouter
from BackenMarca.person_app.views import PersonViewSet

router = DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')
urlpatterns = router.urls
