# Generated by Django 5.0.6 on 2024-07-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('three_app', '0043_teammember'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('order_id', models.CharField(blank=True, max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
