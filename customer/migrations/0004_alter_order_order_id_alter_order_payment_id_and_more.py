# Generated by Django 5.0.2 on 2024-03-26 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='signature_id',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
