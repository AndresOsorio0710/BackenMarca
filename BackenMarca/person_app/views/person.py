from rest_framework import viewsets, mixins
from BackenMarca.person_app.models import Person
from BackenMarca.person_app.serializers import PersonSerializer


class PersonViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
