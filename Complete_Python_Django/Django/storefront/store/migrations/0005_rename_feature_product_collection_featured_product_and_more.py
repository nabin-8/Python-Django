# Generated by Django 5.1.2 on 2024-10-19 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20241019_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='feature_product',
            new_name='featured_product',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='place_at',
            new_name='placed_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='collections',
            new_name='collection',
        ),
    ]
