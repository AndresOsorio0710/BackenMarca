from django.db.models import F
from rest_framework import viewsets, mixins
from product_sale_app.models import ProductSale
from product_sale_app.serializers import SaveProductSaleSerializer, ProductSaleListSerializer, ProductSaleSerializer


class ProductSaleViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = ProductSale.objects.all()
    serializer_class = ProductSaleSerializer

    def get_queryset(self):
        queryset = super(ProductSaleViewSet, self).get_queryset()

        if self.action == self.list.__name__:
            queryset = queryset.values(
                'uuid',
                'name',
                'description',
                'cost',
                'price',
                'utility',
                'discount',
                'discount_unit',
                'show'
            ).annotate(
                sectionName=F('section__name'),
                section=F('section'),
                collectionName=F('collection__name'),
                collection=F('collection')
            )

        return queryset

    def get_serializer_class(self):
        serializer = {
            'create': SaveProductSaleSerializer,
            'list': ProductSaleListSerializer
        }

        if self.action in serializer:
            return serializer[self.action]

        return ProductSaleSerializer
