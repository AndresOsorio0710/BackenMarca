from rest_framework.routers import DefaultRouter
from user_app.views import UserViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
urlpatterns = router.urls
