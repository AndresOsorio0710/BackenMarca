from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models
from product_in_cellar_app.models import ProductInCellar


class ProductInCellarDetail(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    product_in_cellar = models.ForeignKey(ProductInCellar, on_delete=models.PROTECT)
    type = models.CharField(default='CLOTHING', max_length=20)
    size = models.CharField(default='NONE', max_length=20)
    state = models.CharField(default='OK', max_length=20)
    info = models.TextField(default='OK')
