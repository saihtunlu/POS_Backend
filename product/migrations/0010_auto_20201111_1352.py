# Generated by Django 3.1.1 on 2020-11-11 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20201111_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='stock',
        ),
        migrations.AddField(
            model_name='product',
            name='is_tracking',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='variation',
            name='is_tracking',
            field=models.BooleanField(default=False),
        ),
    ]