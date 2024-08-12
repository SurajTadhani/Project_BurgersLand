# Generated by Django 5.0.6 on 2024-06-26 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('three_app', '0027_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodsnackitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('price', models.CharField(max_length=100, null=True)),
                ('content', models.TextField()),
                ('btn', models.CharField(max_length=100)),
            ],
        ),
    ]
