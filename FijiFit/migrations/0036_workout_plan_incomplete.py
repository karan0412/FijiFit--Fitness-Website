# Generated by Django 4.2.3 on 2023-10-19 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FijiFit', '0035_workout_plan_date_workout_plan_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='Plan_incomplete',
            field=models.BooleanField(default=False),
        ),
    ]