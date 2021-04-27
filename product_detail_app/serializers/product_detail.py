from rest_framework import serializers
from product_detail_app.models import ProductDetail


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'
        read_only_fields = ['uuid']


class ProductListSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    cellar = serializers.CharField()
    cellarName = serializers.CharField()
    productInCellar = serializers.CharField()
    productInCellarName = serializers.CharField()
    productSale = serializers.CharField()
    productSaleName = serializers.CharField()
    section = serializers.CharField()
    sectionName = serializers.CharField()
    collection = serializers.CharField()
    collectionName = serializers.CharField()
    amount = serializers.IntegerField()
