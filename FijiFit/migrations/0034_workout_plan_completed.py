# Generated by Django 4.2.3 on 2023-10-19 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FijiFit', '0033_sets'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='Plan_completed',
            field=models.BooleanField(default=False),
        ),
    ]