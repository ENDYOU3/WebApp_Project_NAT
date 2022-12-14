# Generated by Django 4.0.5 on 2022-08-08 12:16

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
                ('code_product', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('product_type', models.CharField(choices=[('Planet', 'Planet'), ('Dwarf Planet', 'Dwarf Planet')], max_length=50)),
                ('quantity', models.IntegerField(null=True)),
                ('price', models.IntegerField()),
                ('special_price', models.IntegerField(blank=True, null=True)),
                ('is_premium', models.BooleanField(default=False)),
                ('promotion_end', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, default='default.png', null=True, upload_to='image_product')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
