# Generated by Django 3.1.1 on 2020-11-10 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_variation_sold_out'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(max_length=2000, null=True)),
                ('products', models.ManyToManyField(to='product.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OptionValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(max_length=2000, null=True)),
                ('color_code', models.TextField(max_length=2000, null=True)),
                ('image', models.ImageField(null=True, upload_to='products/option/')),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='values', to='product.option')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='AttributeValue',
        ),
        migrations.AddField(
            model_name='product',
            name='options',
            field=models.ManyToManyField(blank=True, to='product.Option'),
        ),
    ]
