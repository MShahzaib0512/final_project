# Generated by Django 5.1.1 on 2024-09-28 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0014_rename_top_catogery_brand_top_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='permoted_item',
            field=models.BooleanField(default=False),
        ),
    ]
