# Generated by Django 4.1.4 on 2022-12-31 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_promotion_featured_product_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='featured_product_id',
            new_name='featured_product',
        ),
    ]
