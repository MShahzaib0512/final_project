# Generated by Django 5.1.1 on 2024-10-14 05:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0022_alter_cart_grand_total_alter_cart_total_adress'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=100)),
                ('area_code', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('zip_code', models.IntegerField()),
                ('company', models.CharField(blank=True, max_length=20, null=True)),
                ('bussiness', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Adress',
        ),
    ]
