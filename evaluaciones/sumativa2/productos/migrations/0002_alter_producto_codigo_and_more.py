# Generated by Django 5.1.1 on 2024-09-24 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.CharField(default='Sin Código', max_length=20),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]