# Generated by Django 3.1.1 on 2020-11-11 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_auto_20201111_1023'),
        ('product', '0008_auto_20201111_0039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='gtin',
            new_name='barcode',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='image',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='margin',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='markup',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='vendor',
        ),
        migrations.AddField(
            model_name='product',
            name='available_stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='buying_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='has_variant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='length',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='margin',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='markup',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='number_of_stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='selling_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sold_out',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='threshold_stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='vendor.vendor'),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='width',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
