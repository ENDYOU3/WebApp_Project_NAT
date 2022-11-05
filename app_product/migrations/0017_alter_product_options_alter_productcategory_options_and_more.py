# Generated by Django 4.1 on 2022-10-29 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0016_rename_product_category_productcategory_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'All Product'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name_plural': 'Type'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='code_product',
            new_name='code',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_type',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_product.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_product.producttype'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=225),
        ),
        migrations.DeleteModel(
            name='NewProduct',
        ),
    ]
