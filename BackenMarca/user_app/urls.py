from rest_framework.routers import DefaultRouter
from BackenMarca.user_app.views import UserViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
urlpatterns = router.urls
