from uuid import uuid4
from django.db import models
from django_paranoid.models import ParanoidModel
from BackenMarca.cellar_app.models import Cellar
from BackenMarca.provider_app.models import Provider


class ProductInCellar(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    cellar = models.ForeignKey(Cellar, on_delete=models.PROTECT)  # bodega
    provider = models.ForeignKey(Provider, on_delete=models.PROTECT)  # proveedor
    reference = models.CharField(max_length=20, default='NOT')
    name = models.CharField(max_length=50, default='NOT INCLUDED')  # nombre
    description = models.TextField(default='NOT INCLUDED')  # descripcion
    cost = models.DecimalField(default=0, decimal_places=2, max_digits=8)  # costo
    unit_cost = models.DecimalField(default=0, decimal_places=2, max_digits=7)  # costo unitario
    quantity_entered = models.PositiveIntegerField(default=0)  # cantidad ingresada
    free_quantity = models.PositiveIntegerField(default=0)
    stop = models.PositiveIntegerField(default=0)  # cantidad minima permitida
    show = models.BooleanField(default=False)  # campo utilizado para mostrar u ocultar informacion
