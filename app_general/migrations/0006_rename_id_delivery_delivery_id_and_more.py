# Generated by Django 4.1 on 2022-11-02 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0005_rename_customer_id_delivery_customer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delivery',
            old_name='id',
            new_name='delivery_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='id',
            new_name='order_id',
        ),
    ]
