# Generated by Django 5.1.1 on 2024-09-25 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_brand_image_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='trending',
            field=models.BooleanField(default=False),
        ),
    ]
