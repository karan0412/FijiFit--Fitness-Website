# Generated by Django 4.2.3 on 2023-10-19 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FijiFit', '0037_workout_plan_setdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='Plan_setTime',
            field=models.DateTimeField(null=True),
        ),
    ]