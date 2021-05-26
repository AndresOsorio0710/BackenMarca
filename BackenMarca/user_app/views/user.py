from django.db.models import F
from rest_framework import viewsets, mixins
from BackenMarca.user_app.models import User
from BackenMarca.user_app.serializers import UserSerializer, UserListSerializer, SaveUserSerializer


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = super(UserViewSet, self).get_queryset()

        if self.action == self.list.__name__:
            queryset = queryset.values(
                'uuid',
                'email',
                'phone_number',
                'name',
                'role',
                'person'
            ).annotate(
                personName=F('person__name'),
                personLastName=F('person__last_name'),
                personEmail=F('person__email'),
                personPhoneNumber=F('person__phone_number'),
                personAddress=F('person__address'),
            )

        return queryset

    def get_serializer_class(self):
        serializer = {
            'create': SaveUserSerializer,
            'list': UserListSerializer
        }
        if self.action in serializer:
            return serializer[self.action]

        return UserSerializer
