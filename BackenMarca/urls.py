from django.urls import path, include

urlpatterns = [
    path('', include('BackenMarca.access_control.urls')),
    path('', include('BackenMarca.cellar_app.urls')),
    path('', include('BackenMarca.provider_app.urls')),
    path('', include('BackenMarca.product_in_cellar_app.urls')),
    path('', include('BackenMarca.product_in_cellar_detail_app.urls')),
    path('', include('BackenMarca.collection_app.urls')),
    path('', include('BackenMarca.section_app.urls')),
    path('', include('BackenMarca.product_sale_app.urls')),
    path('', include('BackenMarca.product_detail_app.urls')),
    path('', include('BackenMarca.person_app.urls')),
    path('', include('BackenMarca.employee_app.urls')),
    path('', include('BackenMarca.client_app.urls')),
    path('', include('BackenMarca.user_app.urls'))
]
