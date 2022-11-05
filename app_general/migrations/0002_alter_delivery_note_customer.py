# Generated by Django 4.1 on 2022-10-31 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='note',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('country', models.CharField(max_length=225)),
                ('city', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=225)),
                ('phone', models.CharField(max_length=225)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]