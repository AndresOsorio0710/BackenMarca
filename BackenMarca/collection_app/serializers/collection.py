from rest_framework import serializers
from BackenMarca.collection_app.models import Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
        read_only_fields = ['uuid']


class CollectionLiteSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField(max_length=50)
    icon = serializers.CharField(max_length=50)
