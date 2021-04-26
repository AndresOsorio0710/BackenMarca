# Generated by Django 3.2 on 2021-04-25 23:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_in_cellar_app', '0002_productincellar_free_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInCellarDetail',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantity_entered', models.PositiveIntegerField(default=0)),
                ('free_quantity', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(default='NOT INCLUDED')),
                ('product_in_cellar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product_in_cellar_app.productincellar')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]