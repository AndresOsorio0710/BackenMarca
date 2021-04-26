from rest_framework.routers import DefaultRouter
from product_in_cellar_app.views import ProductInCellarViewSet

router = DefaultRouter()
router.register(r'pic', ProductInCellarViewSet, basename='pic')
urlpatterns = router.urls
