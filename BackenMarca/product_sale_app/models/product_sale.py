from uuid import uuid4
from django.db import models
from django_paranoid.models import ParanoidModel
from BackenMarca.section_app.models import Section
from BackenMarca.collection_app.models import Collection


class ProductSale(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, default='NOT INCLUDED')
    description = models.TextField(default='NOT INCLUDED')
    cost = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    utility = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    discount = models.IntegerField(default=0)
    discount_unit = models.IntegerField(default=0)
    show = models.BooleanField(default=False)
