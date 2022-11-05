# Generated by Django 4.0.5 on 2022-08-08 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('description', models.TextField()),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('unapprove', 'Unapprove'), ('approve', 'Approve'), ('banned', 'Banned')], default='unapprove', max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('note', models.TextField(max_length=100, null=True)),
                ('payment_method', models.CharField(choices=[('cash on delivery', 'Cash On Delivery'), ('bank transfer', 'Bank Transfer')], default='Cash On Delivery', max_length=50)),
                ('quantity_product', models.IntegerField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_product', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('Order_to_Delivery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_general.delivery')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
