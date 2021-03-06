"""BackenMarca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cellar_app.urls')),
    path('api/', include('provider_app.urls')),
    path('api/', include('product_in_cellar_app.urls')),
    path('api/', include('product_in_cellar_detail_app.urls')),
    path('api/', include('collection_app.urls')),
    path('api/', include('section_app.urls')),
    path('api/', include('product_sale_app.urls')),
    path('api/', include('product_detail_app.urls')),
    path('api/', include('person_app.urls')),
    path('api/', include('employee_app.urls')),
    path('api/', include('client_app.urls')),
    path('api/', include('user_app.urls'))
]
