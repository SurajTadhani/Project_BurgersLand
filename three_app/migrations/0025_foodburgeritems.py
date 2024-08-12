# Generated by Django 5.0.6 on 2024-06-25 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('three_app', '0024_homefoodbeverages_homefoodpizza_homefoodsnack'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodburgeritems',
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