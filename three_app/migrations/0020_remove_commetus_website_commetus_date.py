# Generated by Django 5.0.6 on 2024-06-24 08:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('three_app', '0019_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commetus',
            name='website',
        ),
        migrations.AddField(
            model_name='commetus',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
