from rest_framework.routers import DefaultRouter
from BackenMarca.employee_app.views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet, basename='employee')
urlpatterns = router.urls
