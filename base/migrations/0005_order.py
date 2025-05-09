# Generated by Django 5.2 on 2025-04-11 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_cartmodel_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('payment_method', models.CharField(choices=[('COD', 'Cash on Delivery'), ('Online', 'Online Payment')], max_length=10)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
