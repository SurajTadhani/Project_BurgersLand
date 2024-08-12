# Generated by Django 5.0.6 on 2024-07-02 07:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('three_app', '0040_pizzanutrition_pizza'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.URLField()),
                ('category', models.CharField(max_length=50)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='three_app.pizza')),
            ],
        ),
    ]