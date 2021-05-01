from rest_framework import serializers
from product_in_cellar_app.models import ProductInCellar
import random


class ProductInCellarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCellar
        fields = '__all__'
        read_only_fields = ['uuid']


class ProductListSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    cellarName = serializers.CharField()
    cellar = serializers.CharField()
    providerName = serializers.CharField()
    provider = serializers.CharField()
    name = serializers.CharField()
    reference = serializers.CharField()
    description = serializers.CharField()
    cost = serializers.FloatField()
    unit_cost = serializers.FloatField()
    quantity_entered = serializers.IntegerField()
    free_quantity = serializers.IntegerField()
    stop = serializers.IntegerField()
    show = serializers.BooleanField()


class SaveProductInCellarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCellar
        fields = ['cellar',
                  'provider',
                  'name',
                  'cost',
                  'quantity_entered',
                  'stop',
                  'description'
                  ]

    def validate(self, attrs):
        if attrs.get('cellar').free_capacity < attrs.get('quantity_entered'):
            raise serializers.ValidationError({
                "status": "La cantidad ingresada excede la capacidad disponible de la bodega. "
            })
        name = attrs.get('name').upper()
        pre = name[0:4]
        rabd = random.randint(0, 9999)
        attrs.update({
            'unit_cost': attrs.get('cost') / attrs.get('quantity_entered'),
            'free_quantity': 0,
            'reference': pre + "-" + "{:0>3}".format(str(len(name))) + "-" + "{:0>4}".format(str(rabd))
        })
        return attrs
