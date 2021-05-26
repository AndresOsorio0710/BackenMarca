from rest_framework import viewsets, mixins
from BackenMarca.client_app.models import Client
from BackenMarca.client_app.serializers import ClientSerializer


class ClientViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
