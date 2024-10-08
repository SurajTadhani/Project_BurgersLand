# Generated by Django 5.0.6 on 2024-06-10 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('three_app', '0009_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('guest_count', models.IntegerField(choices=[(1, '1 Guest'), (2, '2 Guests'), (3, '3 Guests'), (4, '4 Guests'), (5, '5 Guests')])),
            ],
        ),
        migrations.DeleteModel(
            name='homebookingtable',
        ),
    ]
