# Generated by Django 2.2 on 2020-04-10 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_userprofilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofilefeeditem',
            old_name='user',
            new_name='user_profile',
        ),
    ]
