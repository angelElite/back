# Generated by Django 4.2.5 on 2023-10-31 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_red', '0002_redesipv4_router'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitoreo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEmisor', models.CharField(max_length=100)),
                ('direccionIp', models.GenericIPAddressField()),
                ('fabricante', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=100)),
                ('contrasenia', models.CharField(max_length=100)),
                ('monitireSNP', models.BooleanField()),
                ('comunidadSNP', models.CharField(max_length=50)),
                ('versionSNP', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NapCaja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=200)),
                ('capacidad', models.IntegerField()),
                ('fecha_instalacion', models.DateField()),
                ('proveedor_internet', models.CharField(max_length=100)),
                ('en_operacion', models.BooleanField(default=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
