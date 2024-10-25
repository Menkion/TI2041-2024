# Generated by Django 5.1.1 on 2024-10-23 01:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_caracteristica_producto_caracteristica_valor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCaracteristica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='caracteristica',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='caracteristicas',
        ),
        migrations.AlterField(
            model_name='caracteristica',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='caracteristicas', to='productos.producto'),
        ),
        migrations.AddField(
            model_name='caracteristica',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='productos.tipocaracteristica'),
            preserve_default=False,
        ),
    ]
