from django.contrib.auth import logout
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class AccessControlView(GenericViewSet):

    @action(methods=['POST'], detail=False, url_path='register', url_name='register')
    def user_register(self, request, *args, **kwargs):
        return Response('Me voy a la mierda')

    @action(detail=False, methods=['GET'], url_path='logout', url_name='logout')
    def user_logout(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        logout(request)

        return Response('User Logged out successfully')
