# Generated by Django 5.0 on 2023-12-29 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0002_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='area',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
