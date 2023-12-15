from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    Recipe_id = models.AutoField
    Recipe_title = models.CharField(max_length = 100, unique=True, null=True, blank=True,)
    Recipe_desc = models.CharField(max_length = 5000, null=True, blank=True,)
    Recipe_img= models.ImageField(null=True, blank=True, upload_to='media/')
    Recipe_ing = models.CharField(max_length = 5000, null=True, blank=True,)
    category = models.CharField(
        max_length=20,
        choices=[('underweight', 'Underweight'), ('normal', 'Normal'), ('overweight', 'Overweight'), ('obese', 'Obese')], 
        null=True, blank=True,
    )
    def __str__ (self):
        return self.Recipe_title
    
class BMI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id= models.AutoField
    Height = models.FloatField(max_length= 5, null=True, blank=True)
    Weight = models.FloatField(max_length= 5, null=True, blank=True)
    bmi = models.FloatField(max_length= 5, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return str(self.bmi)

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    id= models.AutoField
    date_submitted = models.DateField(auto_now_add=True)

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    Plan_id = models.AutoField
    Plan_title = models.CharField(max_length = 100, unique=True, null=True, blank=True)
    Plan_desc = models.CharField(max_length = 5000, null=True, blank=True,)
    Plan_completed = models.BooleanField(default=False)
    Plan_incomplete = models.BooleanField(default=False)
    Plan_setDateTime = models.DateTimeField(null=True)
    def __str__ (self):
        return str(self.Plan_title)

class Exercise(models.Model):   
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises", null=True, blank=True)
    Exercise_id = models.AutoField
    Exercise_title = models.CharField(max_length = 100)
    def __str__ (self):
        return str(self.Exercise_title)

class RecWorkout(models.Model):
    RecPlan_id = models.AutoField
    RecPlan_title = models.CharField(max_length = 100, unique=True, null=True, blank=True,)
    RecPlan_desc = models.CharField(max_length = 5000, null=True, blank=True,)
    RecPlan_img= models.ImageField(null=True, blank=True, upload_to='media/')
    categoryWrk = models.CharField(
        max_length=20,
        choices=[('underweight', 'Underweight'), ('normal', 'Normal'), ('overweight', 'Overweight'), ('obese', 'Obese')], 
        null=True, blank=True,
    )
    def __str__ (self):
        return str(self.RecPlan_title)
    
class RecExercise(models.Model):
    workoutRec = models.ForeignKey(RecWorkout, on_delete=models.CASCADE, null=True, blank=True, related_name="recExercises")   
    RecEx_id = models.AutoField
    RecEx_title = models.CharField(max_length = 100, null=True, blank=True,)
    def __str__ (self):
        return str(self.RecEx_title)
    
class Sets(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="sets", null=True, blank=True,)
    sets_reps_Text = models.CharField(max_length = 100, null=True, blank=True,)
    def __str__ (self):
        return str(self.sets_reps_Text)