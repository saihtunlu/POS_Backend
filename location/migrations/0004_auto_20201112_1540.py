# Generated by Django 3.1.1 on 2020-11-12 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_auto_20201111_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationproduct',
            name='quantity',
            field=models.TextField(default='0', max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='locationproduct',
            name='sold_out',
            field=models.TextField(default='0', max_length=2000, null=True),
        ),
    ]
