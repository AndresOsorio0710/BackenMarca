from rest_framework import serializers
from BackenMarca.provider_app.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'
        read_only_fields = ['uuid']


class LiteProviderSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField(max_length=100)
