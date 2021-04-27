from rest_framework import serializers
from user_app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['uuid']


class UserListSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    name = serializers.CharField()
    role = serializers.CharField()
    person = serializers.CharField()
    personName = serializers.CharField()
    personLastName = serializers.CharField()
    personEmail = serializers.EmailField()
    personPhoneNumber = serializers.CharField()
    personAddress = serializers.CharField()


class SaveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'person',
            'name',
            'email',
            'role',
            'phone_number',
            'password'
        ]

    def validate(self, attrs):
        attrs.update({
            'password_old': attrs.get('password')
        })
        return attrs
