from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from BackenMarca.collection_app.models import Collection
from BackenMarca.collection_app.serializers import CollectionSerializer, CollectionLiteSerializer


class CollectionViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_queryset(self):
        queryset = super(CollectionViewSet, self).get_queryset()
        if self.action == self.get_lite.__name__:
            queryset = queryset.only('uuid', 'name', 'icon')
        return queryset

    def get_serializer_class(self):
        serializer = {
            'get_lite': CollectionLiteSerializer
        }
        if self.action in serializer:
            return serializer[self.action]
        return CollectionSerializer

    @action(methods=['GET'], detail=False, url_name='lite', url_path='lite', name='lite')
    def get_lite(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
