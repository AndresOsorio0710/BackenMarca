from uuid import uuid4
from django.db import models
from django_paranoid.models import ParanoidModel
from product_in_cellar_app.models import ProductInCellar
from product_sale_app.models import ProductSale


class ProductDetail(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    product_in_cellar = models.ForeignKey(ProductInCellar, on_delete=models.PROTECT)
    product_sale = models.ForeignKey(ProductSale, on_delete=models.PROTECT)
    amount = models.IntegerField(default=0)
