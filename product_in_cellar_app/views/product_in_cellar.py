from django.db.models import F, Sum
from rest_framework import viewsets, mixins
from product_in_cellar_app.models import ProductInCellar
from product_in_cellar_app.serializers import ProductInCellarSerializer, SaveProductInCellarSerializer, \
    ProductListSerializer


class ProductInCellarViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = ProductInCellar.objects.all()
    serializer_class = ProductInCellarSerializer

    def get_queryset(self):
        queryset = super(ProductInCellarViewSet, self).get_queryset()

        if self.action == self.list.__name__:
            queryset = queryset.values(
                'uuid',
                'name',
                'reference',
                'description',
                'cost',
                'unit_cost',
                'quantity_entered',
                'free_quantity',
                'stop',
                'show'
            ).annotate(
                cellarName=F('cellar__name'),
                cellar=F('cellar'),
                providerName=F('provider__name'),
                provider=F('provider')
            ).order_by('name')

        return queryset

    def get_serializer_class(self):
        serializer = {
            'create': SaveProductInCellarSerializer,
            'list': ProductListSerializer
        }

        if self.action in serializer:
            return serializer[self.action]

        return ProductInCellarSerializer
