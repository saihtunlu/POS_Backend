# Generated by Django 3.1.1 on 2020-11-13 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_auto_20201113_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='height_unit',
            new_name='demission_unit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='length_unit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='width_unit',
        ),
    ]