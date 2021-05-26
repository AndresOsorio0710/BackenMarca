from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models


class Cellar(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=50, default='NOT INCLUDED')
    description = models.TextField(default='NOT INCLUDED')
    max_capacity = models.PositiveIntegerField(default=0)
    free_capacity = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=80, default='NOT INCLUDED')
    phone_number = models.CharField(max_length=10, default='NOT INCLUDED')
    email = models.EmailField(default='notIncluded@marca.com')
    show = models.BooleanField(default=False)