# Generated by Django 4.2.5 on 2023-11-10 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_red', '0009_alter_oltdevice_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oltdevice',
            name='snmp_port',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='oltdevice',
            name='telnet_port',
            field=models.CharField(max_length=100),
        ),
    ]
