# Generated by Django 5.1.1 on 2024-10-23 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_caracteristica_categoria_marca_alter_producto_codigo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caracteristica',
            old_name='tipo',
            new_name='nombre',
        ),
    ]