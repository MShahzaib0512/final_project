# Generated by Django 5.1.1 on 2024-09-27 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0013_products_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='top_catogery',
            new_name='top_brand',
        ),
    ]
