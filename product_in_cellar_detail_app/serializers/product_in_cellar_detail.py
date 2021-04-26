from rest_framework import serializers
from product_in_cellar_detail_app.models import ProductInCellarDetail


class ProductInCellarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCellarDetail
        fields = '__all__'
        read_only_fields = ['uuid']


class ProductListSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    product = serializers.CharField()
    productName = serializers.CharField()
    cellarName = serializers.CharField()
    quantity_entered = serializers.IntegerField()
    free_quantity = serializers.IntegerField()
    description = serializers.CharField()


class SaveProductInCellarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCellarDetail
        fields = ['product_in_cellar',
                  'quantity_entered',
                  'description'
                  ]

    def validate(self, attrs):
        if attrs.get('product_in_cellar').free_quantity < attrs.get('quantity_entered'):
            raise serializers.ValidationError({
                "status": "Cantidad invalida, excede la cantidad no asociada del producto en bodega."
            })
        attrs.update({
            'free_quantity': attrs.get('quantity_entered')
        })
        return attrs
