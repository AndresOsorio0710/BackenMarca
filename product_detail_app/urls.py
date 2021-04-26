from rest_framework.routers import DefaultRouter
from product_detail_app.views import ProductDetailViewSet

router = DefaultRouter()
router.register(r'pd', ProductDetailViewSet, basename='pd')
urlpatterns = router.urls
