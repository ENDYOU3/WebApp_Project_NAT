# Generated by Django 4.1 on 2022-11-02 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0004_rename_order_date_delivery_delivery_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='delivery',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product_id',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='delivery',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]