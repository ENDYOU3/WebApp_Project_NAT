# Generated by Django 4.1 on 2022-11-02 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_general', '0011_alter_order_delivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_general.delivery'),
        ),
    ]