# Generated by Django 4.2 on 2023-05-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_options_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=None, max_length=300),
        ),
    ]
