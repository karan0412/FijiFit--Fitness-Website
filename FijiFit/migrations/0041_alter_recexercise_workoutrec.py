# Generated by Django 4.2.4 on 2023-10-22 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FijiFit', '0040_remove_workout_plan_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recexercise',
            name='workoutRec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recExercises', to='FijiFit.recworkout'),
        ),
    ]
