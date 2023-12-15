# Generated by Django 4.2.3 on 2023-10-29 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FijiFit', '0041_alter_recexercise_workoutrec'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='Plan_setTime',
        ),
        migrations.AlterField(
            model_name='bmi',
            name='Height',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='bmi',
            name='Weight',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='bmi',
            name='bmi',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='recexercise',
            name='RecEx_title',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='Recipe_desc',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='Recipe_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='Recipe_ing',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='Recipe_title',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='recworkout',
            name='RecPlan_desc',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='recworkout',
            name='RecPlan_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='recworkout',
            name='RecPlan_title',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='sets',
            name='sets_reps_Text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='Plan_setDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='Plan_title',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
