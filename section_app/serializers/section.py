from rest_framework import serializers
from section_app.models import Section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
        read_only_fields = ['uuid']


class SectionLiteSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField(max_length=50)
    icon = serializers.CharField(max_length=50)
