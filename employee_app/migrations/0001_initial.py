# Generated by Django 3.2 on 2021-04-26 06:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.CharField(default='CASHIER', max_length=20)),
                ('min_salary', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('sales_commission', models.IntegerField(default=0)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='person_app.person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
