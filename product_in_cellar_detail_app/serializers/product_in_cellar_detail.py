from rest_framework import serializers
from product_in_cellar_app.models import ProductInCellar
from product_in_cellar_detail_app.models import ProductInCellarDetail
from django.db.models import Count


class ProductInCellarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCellarDetail
        fields = '__all__'
        read_only_fields = ['uuid']


class ListSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    product = serializers.CharField()
    name = serializers.CharField()
    cellar = serializers.CharField()
    provider = serializers.CharField()
    reference = serializers.CharField()
    type = serializers.CharField()
    size = serializers.CharField()
    state = serializers.CharField()
    info = serializers.CharField()


class PICListSerializer(serializers.Serializer):
    product_in_cellar = serializers.CharField()
    name = serializers.CharField()
    cellar = serializers.CharField()
    provider = serializers.CharField()
    reference = serializers.CharField()
    description = serializers.CharField()
    cost = serializers.FloatField()
    unit_cost = serializers.FloatField()
    quantity = serializers.IntegerField()
    free = serializers.IntegerField()
    stop = serializers.IntegerField()


class PICSizeListSerializer(serializers.Serializer):
    size = serializers.CharField()
    free = serializers.IntegerField()


class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCellarDetail
        fields = ['product_in_cellar',
                  'type',
                  'size',
                  'state',
                  'info'
                  ]

    def validate(self, attrs):
        if attrs.get('product_in_cellar').free_quantity == attrs.get('product_in_cellar').quantity_entered:
            raise serializers.ValidationError({
                "status": "El producto ya fue segcionado y relacionado. "
            })
        return attrs
