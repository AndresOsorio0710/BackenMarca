from rest_framework import serializers
from BackenMarca.employee_app.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ['uuid']
