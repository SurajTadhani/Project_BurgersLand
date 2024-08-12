# Generated by Django 5.0.6 on 2024-06-28 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('three_app', '0035_burger_category_snack_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodbeverages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('content', models.TextField()),
                ('price', models.CharField(max_length=100, null=True)),
                ('btn', models.CharField(max_length=20)),
            ],
        ),
    ]
