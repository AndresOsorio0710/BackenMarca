from django.db.models import F
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from product_in_cellar_detail_app.models import ProductInCellarDetail
from product_in_cellar_detail_app.serializers import ProductInCellarDetailSerializer, \
    SaveProductInCellarDetailSerializer, \
    ProductListSerializer


class ProductInCellarDetailViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = ProductInCellarDetail.objects.all()
    serializer_class = ProductInCellarDetailSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        queryset = super(ProductInCellarDetailViewSet, self).get_queryset()

        if self.action == self.list.__name__:
            queryset = queryset.values(
                'uuid',
                'quantity_entered',
                'free_quantity',
                'description',
            ).annotate(
                product=F('product_in_cellar'),
                productName=F('product_in_cellar__name'),
                cellarName=F('product_in_cellar__cellar__name')
            )

        if self.action == self.get_pic.__name__:
            queryset = queryset.filter(
                product_in_cellar=self.kwargs.get('uuid')
            ).values(
                'uuid',
                'quantity_entered',
                'free_quantity',
                'description',
            ).annotate(
                product=F('product_in_cellar'),
                productName=F('product_in_cellar__name'),
                cellarName=F('product_in_cellar__cellar__name')
            )

        return queryset

    def get_serializer_class(self):
        serializer = {
            'create': SaveProductInCellarDetailSerializer,
            'list': ProductListSerializer,
            'get_pic': ProductListSerializer
        }

        if self.action in serializer:
            return serializer[self.action]

        return ProductInCellarDetailSerializer

    @action(methods=['GET'], detail=True, url_name='pic', url_path='pic', name='pic')
    def get_pic(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
