# Generated by Django 4.1 on 2022-08-21 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0002_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]