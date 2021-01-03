# Generated by Django 3.1.2 on 2020-11-20 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('sex', models.CharField(choices=[('W', 'Female'), ('M', 'Male'), ('U', 'Unisex')], default='U', max_length=7)),
                ('p_type', models.CharField(blank=True, max_length=50, null=True)),
                ('image_link', models.CharField(blank=True, max_length=500, null=True)),
                ('stock_price', models.DecimalField(decimal_places=2, default=999.0, max_digits=10)),
                ('show', models.BooleanField(default=False)),
                ('in_stock', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('volume', models.CharField(blank=True, max_length=50, null=True)),
                ('score', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=999.0, max_digits=100)),
                ('brand_name', models.ForeignKey(default='Brand Name', on_delete=django.db.models.deletion.CASCADE, related_name='brand_name', to='product.brand', to_field='name')),
            ],
        ),
    ]