from typing import Self
from django.db.models import Q
from django.http import HttpResponse, HttpResponseForbidden
from .models import Recipe
from .models import User, Submission
from .models import BMI
from .models import Workout
from .models import RecWorkout
from .models import Exercise
from .models import RecExercise
from .models import Sets
import pytz
from django.shortcuts import get_object_or_404, render, redirect
from datetime import date, timedelta, datetime
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def Home(request):
    return render(request, 'Home.html')

def Index (request):
    return render(request, 'index.html')

def completedPlan (request):
    completed_workouts = Workout.objects.filter(user=request.user, Plan_completed=True)
    context = {
      "completed_workouts":completed_workouts,
    }
        
    return render(request, 'CompletedPlan.html', context)

def incompletedPlan (request):
    incompleted_workouts = Workout.objects.filter(user=request.user,Plan_incomplete=True, Plan_completed=False)
    context = {
      "incompleted_workouts":incompleted_workouts,
    }
        
    return render(request, 'IncompletePlan.html', context)

@login_required
def MealRec (request):
    try:
        user_bmi_instance = BMI.objects.filter(user=request.user).latest('date')
        user_bmi_value = user_bmi_instance.bmi
    except:
        return render(request, 'Dashboard.html', {'message': 'Please enter your BMI first.'})

    if user_bmi_value < 18.5:
        meals = Recipe.objects.filter(category='underweight')
    elif 18.5 <= user_bmi_value < 25:
        meals = Recipe.objects.filter(category='normal')
    elif 25 <= user_bmi_value < 30:
        meals = Recipe.objects.filter(category='overweight')
    else:
        meals = Recipe.objects.filter(category='obese')

    context = {
        "meals":meals,
    }
    return render(request, 'MealRec.html', context)

@login_required
def WorkoutRec (request):
    try:
        user_bmi_instance = BMI.objects.filter(user=request.user).latest('date')
        user_bmi_value = user_bmi_instance.bmi
    except:
        return render(request, 'Dashboard.html', {'message': 'Please enter your BMI first.'})

    if user_bmi_value < 18.5:
        wrk = RecWorkout.objects.filter(categoryWrk='underweight')
    elif 18.5 <= user_bmi_value < 25:
        wrk = RecWorkout.objects.filter(categoryWrk='normal')
    elif 25 <= user_bmi_value < 30:
        wrk = RecWorkout.objects.filter(categoryWrk='overweight')
    else:
        wrk = RecWorkout.objects.filter(categoryWrk='obese')

    context = {
        "wrk":wrk,
    }
    return render(request, 'WorkoutRec.html', context)


@login_required
def ExerciseRec (request, pk):
    workoutRec = get_object_or_404(RecWorkout, pk=pk)
    exRec = RecExercise.objects.filter(workoutRec=workoutRec)
    context = {
      "exRec":exRec,
    }
        
    return render(request, 'WorkoutPlan.html', context)

@login_required
def PlanWorkout (request):

    if request.method == 'POST':
        WorkoutTitle = (request.POST.get('WorkoutTitle'))
        WorkoutDescription = (request.POST.get('WorkoutDescription')) 
        WorkoutDateTime = (request.POST.get('WorkoutDueDate')) 

        print(f"Received POST data: {WorkoutTitle}, {WorkoutDescription}, {WorkoutDateTime}")
        
        if Workout.objects.filter(Plan_title=WorkoutTitle).exists():
            messages.error(request, "Workout already exists.")
        else:
            Workout.objects.create(user=request.user, Plan_title=WorkoutTitle, Plan_desc=WorkoutDescription, Plan_setDateTime=WorkoutDateTime)
            return redirect('PlanWorkout')

    workouts = Workout.objects.filter(user=request.user)

    for workout in workouts:     

        print(f"Checking workout with Plan_setDateTime: {workout.Plan_setDateTime}")
        print(f"Checking workout with current time: {datetime.now()}")

        if workout.Plan_setDateTime and workout.Plan_setDateTime <= datetime.now():
        
            print(f"Setting Plan_incomplete to True for workout: {workout.id}")
            workout.Plan_incomplete = True
            workout.save()

    obj = Workout.objects.filter(user=request.user, Plan_completed=False, Plan_incomplete=False)
    context = {
        "obj":obj,
        'today_date': datetime.now(),
    }
    
    return render(request, 'WorkoutPlan.html', context)


@login_required
def deleteWorkout(request, pk):
    print("Inside deleteWorkout")
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        workout.delete()
        return redirect("PlanWorkout")
    
    return render(request, 'WorkoutPlan.html', {'workout': workout})

@login_required
def deleteCompleteWorkout(request, pk):
    print("Inside deleteCompleteWorkout")
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        workout.delete()
        return redirect("completedPlan")
    
    return render(request, 'CompletedPlan.html', {'workout': workout})

@login_required
def deleteIncompleteWorkout(request, pk):
    print("Inside deleteIncompleteWorkout")
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == 'POST':
        workout.delete()
        return redirect("incompletedPlan")
    
    return render(request, 'IncompletePlan.html', {'workout': workout})

@login_required
def updateWorkout(request, pk):
    workout = get_object_or_404(Workout, pk=pk, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('WorkoutTitle')
        desc = request.POST.get('WorkoutDescription')
        date = request.POST.get('WorkoutDueDate')

        if Workout.objects.filter(Plan_title=title).exists():
            messages.error(request, "Workout already exists.")
            
        elif title and desc:
            workout.Plan_title = title
            workout.Plan_desc = desc
            workout.Plan_setDate = date

            workout.save()
            return redirect('PlanWorkout')

    return redirect("PlanWorkout")

@login_required
def markComplete(request, workout_id):
    print("Inside markComplete")
    workout = get_object_or_404(Workout, pk=workout_id)
    if request.method == 'POST':
        workout.Plan_completed = True
        workout.save()
        return redirect('completedPlan')


    
@login_required
def deleteExercise(request, pk):
    print("Inside deleteExercise")
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect("PlanWorkout")

def updateExercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)

    if request.method == "POST":
        new_title = request.POST.get('ExerciseTitle')
        if new_title:
            exercise.Exercise_title = new_title
            exercise.save()

        return redirect('PlanWorkout')

@login_required
def addExercise (request, pk):
    workout = get_object_or_404(Workout, pk=pk) 
    if request.method == 'POST':
           
        ExerciseTitle = request.POST.get('ExerciseTitle')
        if ExerciseTitle:
            exercise = Exercise(workout=workout, Exercise_title=ExerciseTitle)
            exercise.save()
        
        print({ExerciseTitle})
        return redirect('PlanWorkout')

    ex = Exercise.objects.filter(workout=workout)
    context = {
      "ex":ex,
    }
        
    return render(request, 'WorkoutPlan.html', context)

def SignUp (request):
    if request.method =='POST':
        user_fname = request.POST.get('user_fname')
        user_lname = request.POST.get('user_lname')
        user_email = request.POST.get('user_email')
        user_username = request.POST.get('user_username')
        user_pwd = request.POST.get('user_pwd')

        if User.objects.filter(username=user_username).exists():
            messages.error(request, "Username already exists! Please Login.")
        elif User.objects.filter(email=user_email).exists():
            messages.error(request, "Email already exists! Please Login.")
        else:
            user = User.objects.create(first_name=user_fname, last_name=user_lname, email=user_email, username=user_username)
            user.set_password(user_pwd) 
            user.save()

            return redirect("Login")
            
    return render(request, 'SignUp.html')

def Login(request):
    if request.method == 'POST':
        username= request.POST.get('uname')
        password = request.POST.get('pwd')
        print({username})
        print({password})
        user = authenticate(request, username=username, password=password)
        print({user})
      
            #user = User.objects.filter(user_email=user_email)
            
            #if user_pwd == user_pwd:    
        if user is not None:     
            login(request, user)    
            return redirect('DashBoard')  # Redirect to dashboard view
        else:
            messages.success(request, ("Please Enter valid credentials"))
    

    return render(request, 'Login.html')


def LogoutUser(request):
    logout(request)
    return redirect('Login')

@login_required
def SideBar (request):
    return render(request, 'SideBar.html')

@login_required
def DashBoard (request):
    #user = request.user
    obj = BMI.objects.filter(user=request.user)
    bmi_value = obj.last().bmi if obj.exists() else None
    def categorize_bmi(bmi):
        if bmi is None:
            return None
        elif bmi < 18.5:
            return 'Underweight. You are not healthy!'
        elif 18.5 <= bmi <= 24.9:
            return 'Normal. You are healthy!'
        elif 25 <= bmi <= 29.9:
            return 'Overweight. You are not healthy!'
        else:
            return 'Obese. You are extremly unhealthy!'

    # Get BMI category
    bmi_category = categorize_bmi(bmi_value)

    context = {
        "obj": obj,
        "bmi_value": bmi_value,
        "bmi_category": bmi_category  # This will contain the BMI category
    }
    return render(request, 'DashBoard.html', context)
    


@login_required
def Cal_BMI(request):
  
    last_week = date.today() - timedelta(days=7)
    yersterday = datetime.today() - timedelta(days=1)
    one_min_ago = timezone.now() - timedelta(minutes=1)

    #recent_entry = BMI.objects.filter(user=request.user, date__gte=last_week).exists()
    #recent_entry = BMI.objects.filter(user=request.user, timestamp__gte=yersterday).exists()
    recent_entry = BMI.objects.filter(user=request.user, timestamp__gte=one_min_ago).exists()

    if recent_entry:
        messages.success(request, ("You have already entered your BMI. Please try again later after 1 week."))
        return redirect("DashBoard")

    else:
        if request.method == 'POST':
            Height = float(request.POST.get('Height'))
            Weight = float(request.POST.get('Weight'))
                
            # Server-side validation
            if Height <= 20.0 or Height >= 200 or Weight <= 10.0 or Weight >= 200 or Height == 0 or Weight == 0:
                messages.error(request, "Invalid Range. Please provide valid values.")
         
            else:
                bmi = round(Weight / ((Height / 100) ** 2),2)
                BMI.objects.create(user=request.user, Weight=Weight, Height=Height, bmi=bmi)
                return redirect("DashBoard")
            
    try:    
        user_profile = BMI.objects.filter(user=request.user).order_by('-timestamp').first()
        height = user_profile.Height
        weight = user_profile.Weight
    except AttributeError:
        height = ""
        weight = ""


    context = {
        'height': height,
        'weight': weight,
    }
            
    return render(request, 'BMI.html', context)

@login_required
def addSetsReps (request, pk):
    exercise = get_object_or_404(Exercise, pk=pk) 
    if request.method == 'POST':
           
        setsReps = request.POST.get('setsReps')
        if setsReps:
            sets = Sets(exercise=exercise, sets_reps_Text=setsReps)
            sets.full_clean()
            sets.save()
        
        print({setsReps})
        return redirect('PlanWorkout')

    exerciseSets = Sets.objects.filter(exercise=exercise)
    context = {
      "exerciseSets":exerciseSets,
    }
        
    return render(request, 'WorkoutPlan.html', context)

@login_required
def deleteSet(request, pk):
    print("Inside deleteSet")
    set = get_object_or_404(Sets, pk=pk)
    if request.method == 'POST':
        set.delete()
        return redirect("PlanWorkout")
    
def updateSet(request, pk):
    set = get_object_or_404(Sets, pk=pk)

    if request.method == "POST":
        new_set = request.POST.get('setText')
        if new_set:
            set.sets_reps_Text = new_set
            set.save()

        return redirect("PlanWorkout")


