# Generated by Django 4.2.5 on 2023-10-31 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_red', '0003_monitoreo_napcaja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoreo',
            name='modelo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
