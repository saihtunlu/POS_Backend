# Generated by Django 3.1.1 on 2020-11-13 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20201112_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category1',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='category1',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category1',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category2',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='category2',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category2',
            name='slug',
        ),
    ]