# Generated by Django 5.1.1 on 2024-10-25 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_rename_nombre_caracteristica_caracteristica_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='caracteristica',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
