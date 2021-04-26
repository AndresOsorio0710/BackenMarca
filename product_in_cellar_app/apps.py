from django.apps import AppConfig


class ProductInCellarAppConfig(AppConfig):
    name = 'product_in_cellar_app'

    def ready(self):
        try:
            import product_in_cellar_app.signals.product_in_cellar
        except ImportError:
            pass
