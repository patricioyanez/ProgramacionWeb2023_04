# Generated by Django 4.2.1 on 2023-05-23 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_alter_cliente_rut'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='dv',
            field=models.CharField(default='', max_length=1),
        ),
    ]
