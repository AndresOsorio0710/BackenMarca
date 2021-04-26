from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models
from product_in_cellar_app.models import ProductInCellar


class ProductInCellarDetail(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    product_in_cellar = models.ForeignKey(ProductInCellar, on_delete=models.PROTECT)
    quantity_entered = models.PositiveIntegerField(default=0)
    free_quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(default='NOT INCLUDED')
