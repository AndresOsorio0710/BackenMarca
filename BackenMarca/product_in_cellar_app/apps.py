from django.apps import AppConfig


class ProductInCellarAppConfig(AppConfig):
    name = 'BackenMarca.product_in_cellar_app'

    def ready(self):
        try:
            import BackenMarca.product_in_cellar_app.signals.product_in_cellar
        except ImportError:
            pass
