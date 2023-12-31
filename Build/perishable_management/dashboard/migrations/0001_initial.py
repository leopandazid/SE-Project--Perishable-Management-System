# Generated by Django 4.2.7 on 2023-11-11 19:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=30, null=True)),
                ('product_name', models.CharField(max_length=30, null=True)),
                ('category', models.CharField(max_length=30, null=True)),
                ('quantity', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.25), django.core.validators.MaxValueValidator(9.0)])),
            ],
        ),
    ]
