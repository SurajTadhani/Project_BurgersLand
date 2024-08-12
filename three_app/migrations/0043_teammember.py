# Generated by Django 5.0.6 on 2024-07-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('three_app', '0042_delete_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('biography', models.TextField()),
                ('skills', models.TextField()),
                ('experience', models.TextField()),
                ('achievements', models.TextField()),
                ('profile_picture', models.ImageField(upload_to='team_pictures/')),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('personal_interests', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
