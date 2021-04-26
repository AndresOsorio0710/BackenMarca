from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from employee_app.models import Employee
from employee_app.serializers import EmployeeSerializer


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