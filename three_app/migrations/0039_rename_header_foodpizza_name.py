# Generated by Django 5.0.6 on 2024-07-01 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('three_app', '0038_foodpizza'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodpizza',
            old_name='header',
            new_name='name',
        ),
    ]
