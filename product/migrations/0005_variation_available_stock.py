# Generated by Django 3.1.1 on 2020-11-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20201110_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='available_stock',
            field=models.IntegerField(default=0),
        ),
    ]
