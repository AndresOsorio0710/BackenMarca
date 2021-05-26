from rest_framework import serializers
from BackenMarca.client_app.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ['uuid']
