# Generated by Django 4.2.4 on 2023-09-25 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FijiFit', '0009_rename_user_submission_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='user_id',
            new_name='user',
        ),
    ]
