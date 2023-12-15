from django.contrib import admin
from .models import Recipe
from .models import Exercise
from .models import BMI,Submission
from .models import Workout
from .models import RecWorkout
from .models import RecExercise
from .models import Sets

# Register your models here.

admin.site.register(Recipe)

admin.site.register(Sets)

admin.site.register(BMI) 

admin.site.register(Submission) 

admin.site.register(Workout)

admin.site.register(RecWorkout)

admin.site.register(Exercise)

admin.site.register(RecExercise)