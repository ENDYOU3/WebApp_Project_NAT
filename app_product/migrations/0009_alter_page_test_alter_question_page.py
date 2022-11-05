# Generated by Django 4.1 on 2022-10-29 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0008_alter_page_test_alter_question_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_product.test'),
        ),
        migrations.AlterField(
            model_name='question',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_product.test'),
        ),
    ]
