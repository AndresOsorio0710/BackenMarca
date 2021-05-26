from django.apps import AppConfig


class ProductInCellarDetailAppConfig(AppConfig):
    name = 'BackenMarca.product_in_cellar_detail_app'

    def ready(self):
        try:
            import BackenMarca.product_in_cellar_detail_app.signals.product_in_cellar_detail
        except ImportError:
            pass
