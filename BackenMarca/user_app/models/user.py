from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models
from BackenMarca.person_app.models import Person


class User(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, default='DEFAULT')
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, default='DEFAULT')
    role = models.CharField(max_length=20, default='CLIENT')
    password = models.TextField()
    password_old = models.TextField()
