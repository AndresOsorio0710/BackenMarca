# Generated by Django 3.2 on 2021-04-26 03:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='NOT INCLUDED', max_length=50)),
                ('description', models.TextField(default='NOT INCLUDED')),
                ('icon', models.CharField(default='far fa-folder', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
