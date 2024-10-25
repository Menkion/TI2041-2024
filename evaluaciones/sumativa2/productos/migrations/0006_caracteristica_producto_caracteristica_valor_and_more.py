# Generated by Django 5.1.1 on 2024-10-23 01:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_alter_producto_caracteristicas'),
    ]

    operations = [
        migrations.AddField(
            model_name='caracteristica',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='caracteristicas_producto', to='productos.producto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='caracteristica',
            name='valor',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='caracteristicas',
            field=models.ManyToManyField(blank=True, related_name='productos', to='productos.caracteristica'),
        ),
    ]