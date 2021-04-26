from rest_framework import serializers
from product_sale_app.models import ProductSale


class ProductSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSale
        fields = '__all__'
        read_only_fields = ['uuid']


class ProductSaleListSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    section = serializers.CharField()
    sectionName = serializers.CharField()
    collection = serializers.CharField()
    collectionName = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    cost = serializers.FloatField()
    price = serializers.FloatField()
    utility = serializers.FloatField()
    discount = serializers.IntegerField()
    discount_unit = serializers.IntegerField()
    show = serializers.BooleanField()


class SaveProductSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSale
        fields = ['section',
                  'collection',
                  'name',
                  'description',
                  'cost',
                  'price',
                  'discount',
                  'discount_unit'
                  ]

    def validate(self, attrs):
        if attrs.get('price') < attrs.get('cost'):
            raise serializers.ValidationError({
                "status": "El precio de venta del producto no puede ser mayor al costo de compra."
            })
        attrs.update({
            'utility': attrs.get('price') - attrs.get('cost')
        })
        return attrs
