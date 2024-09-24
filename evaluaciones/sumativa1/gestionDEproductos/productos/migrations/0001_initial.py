# Generated by Django 5.1.1 on 2024-09-24 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=50)),
                ('fecha_vencimiento', models.DateField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]