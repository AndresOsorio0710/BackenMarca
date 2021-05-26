from rest_framework import viewsets, mixins
from BackenMarca.employee_app.models import Employee
from BackenMarca.employee_app.serializers import EmployeeSerializer


class EmployeeViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer