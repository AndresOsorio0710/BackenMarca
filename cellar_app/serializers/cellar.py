from rest_framework import serializers
from cellar_app.models import Cellar


class CellarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cellar
        fields = '__all__'
        read_only_fields = ['uuid']


class LiteCellarSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField(max_length=50)
    free_capacity = serializers.IntegerField()


class SaveCellarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cellar
        fields = [
            'name',
            'description',
            'address',
            'phone_number',
            'email',
            'max_capacity'
        ]

    def validate(self, attrs):
        attrs.update({
            'free_capacity': attrs.get('max_capacity')
        })
        return attrs