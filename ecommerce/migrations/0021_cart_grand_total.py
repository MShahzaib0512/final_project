# Generated by Django 5.1.1 on 2024-10-07 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0020_cart_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='grand_total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
