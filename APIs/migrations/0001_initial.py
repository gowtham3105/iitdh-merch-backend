# Generated by Django 4.0 on 2021-12-22 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('order_id', models.CharField(max_length=100)),
                ('payment_id', models.CharField(max_length=100)),
                ('product_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Extra Extra Large')], max_length=50)),
                ('quantity', models.IntegerField(default=1)),
                ('order_amount', models.IntegerField()),
                ('order_date', models.DateField()),
                ('order_status', models.CharField(choices=[('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Delivered', 'Delivered'), ('Shipped', 'Shipped')], max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='APIs.product')),
            ],
        ),
    ]