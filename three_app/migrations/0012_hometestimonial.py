# Generated by Django 5.0.6 on 2024-06-11 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('three_app', '0011_homeourteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='hometestimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('content', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
    ]
