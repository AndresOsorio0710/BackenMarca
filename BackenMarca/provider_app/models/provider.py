from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models


class Provider(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    identification = models.CharField(max_length=15, default='NOT INCLUDED')
    name = models.CharField(max_length=100, default='NOT INCLUDED')
    description = models.TextField(default='NOT INCLUDED')
    address = models.CharField(max_length=80, default='NOT INCLUDED')
    phone_number = models.CharField(max_length=12, default='NOT INCLUDED')
    email = models.EmailField(default='notIncluded@marca.com')
    show = models.BooleanField(default=False)