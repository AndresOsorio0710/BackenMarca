from django.db.models import F
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from BackenMarca.product_detail_app.models import ProductDetail
from BackenMarca.product_detail_app.serializers import ProductDetailSerializer, ProductListSerializer


class ProductDetailViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        queryset = super(ProductDetailViewSet, self).get_queryset()

        if self.action == self.list.__name__:
            queryset = queryset.values(
                'uuid',
                'amount'
            ).annotate(
                cellar=F('product_in_cellar__cellar'),
                cellarName=F('product_in_cellar__cellar__name'),
                productInCellar=F('product_in_cellar'),
                productInCellarName=F('product_in_cellar__name'),
                productSale=F('product_sale'),
                productSaleName=F('product_sale__name'),
                section=F('product_sale__section'),
                sectionName=F('product_sale__section__name'),
                collection=F('product_sale__collection'),
                collectionName=F('product_sale__collection__name'),
            )

        if self.action == self.get_pic.__name__:
            queryset = queryset.filter(
                product_in_cellar=self.kwargs.get('uuid')
            ).values(
                'uuid',
                'amount'
            ).annotate(
                cellar=F('product_in_cellar__cellar'),
                cellarName=F('product_in_cellar__cellar__name'),
                productInCellar=F('product_in_cellar'),
                productInCellarName=F('product_in_cellar__name'),
                productSale=F('product_sale'),
                productSaleName=F('product_sale__name'),
                section=F('product_sale__section'),
                sectionName=F('product_sale__section__name'),
                collection=F('product_sale__collection'),
                collectionName=F('product_sale__collection__name'),
            )

        if self.action == self.get_ps.__name__:
            queryset = queryset.filter(
                product_sale=self.kwargs.get('uuid')
            ).values(
                'uuid',
                'amount'
            ).annotate(
                cellar=F('product_in_cellar__cellar'),
                cellarName=F('product_in_cellar__cellar__name'),
                productInCellar=F('product_in_cellar'),
                productInCellarName=F('product_in_cellar__name'),
                productSale=F('product_sale'),
                productSaleName=F('product_sale__name'),
                section=F('product_sale__section'),
                sectionName=F('product_sale__section__name'),
                collection=F('product_sale__collection'),
                collectionName=F('product_sale__collection__name'),
            )

        return queryset

    def get_serializer_class(self):
        serializer = {
            'list': ProductListSerializer,
            'get_pic': ProductListSerializer,
            'get_ps': ProductListSerializer
        }

        if self.action in serializer:
            return serializer[self.action]

        return ProductDetailSerializer

    @action(methods=['GET'], detail=True, url_name='pic', url_path='pic', name='pic')
    def get_pic(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True, url_name='ps', url_path='ps', name='ps')
    def get_ps(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
