from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models

from BackenMarca.person_app.models import Person


class Employee(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    role = models.CharField(max_length=20, default='CASHIER')
    min_salary = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    sales_commission = models.IntegerField(default=0)
