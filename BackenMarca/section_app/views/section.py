from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from BackenMarca.section_app.serializers import SectionSerializer, SectionLiteSerializer
from BackenMarca.section_app.models import Section


class SectionViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def get_queryset(self):
        queryset = super(SectionViewSet, self).get_queryset()
        if self.action == self.get_lite.__name__:
            queryset = queryset.only('uuid', 'name', 'icon')
        return queryset

    def get_serializer_class(self):
        serializer = {
            'get_lite': SectionLiteSerializer
        }
        if self.action in serializer:
            return serializer[self.action]
        return SectionSerializer

    @action(methods=['GET'], detail=False, url_name='lite', url_path='lite', name='lite')
    def get_lite(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
