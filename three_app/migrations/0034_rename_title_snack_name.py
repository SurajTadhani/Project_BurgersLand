# Generated by Django 5.0.6 on 2024-06-27 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('three_app', '0033_delete_foodsnackitems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snack',
            old_name='title',
            new_name='name',
        ),
    ]