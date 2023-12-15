from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [

    path("SignUp/", views.SignUp, name="SignUp"),
    path("LogoutUser/", views.LogoutUser, name="LogoutUser"),
    path("index/", views.Index, name="Index"),
    path("", views.Home, name="Home"),
    path("Login/", views.Login, name="Login"),
    path("MealRec/", views.MealRec, name="MealRecommendations"),  
    path("BMI/", views.Cal_BMI, name="cal_bmi_view"),  
    path("DashBoard/", views.DashBoard, name="DashBoard"), 
    path("siderBar/", views.SideBar, name="Siderbar"),   
    path("WorkoutPlan/", views.PlanWorkout, name="PlanWorkout"),
    path("ExerciseRec/", views.ExerciseRec, name="ExerciseRec"), 
    path("WorkoutRec/", views.WorkoutRec, name="WorkoutRec"),   
    path('deleteWorkout/<int:pk>/', views.deleteWorkout, name='deleteWorkout'),
    path('deleteCompleteWorkout/<int:pk>/', views.deleteCompleteWorkout, name='deleteCompleteWorkout'),
    path('deleteIncompleteWorkout/<int:pk>/', views.deleteIncompleteWorkout, name='deleteIncompleteWorkout'),
    path('updateWorkout/<int:pk>/', views.updateWorkout, name='updateWorkout'),
    path('addExercise/<int:pk>/', views.addExercise, name='addExercise'),
    path('deleteExercise/<int:pk>/', views.deleteExercise, name='deleteExercise'),
    path('updateExercise/<int:exercise_id>/', views.updateExercise, name='updateExercise'),
    path('addSetsReps/<int:pk>/', views.addSetsReps, name='addSetsReps'),
    path('deleteSet/<int:pk>/', views.deleteSet, name='deleteSet'),
    path('updateSet/<int:pk>/', views.updateSet, name='updateSet'),
    path("completedPlan/", views.completedPlan, name="completedPlan"),
    path("incompletedPlan/", views.incompletedPlan, name="incompletedPlan"),
    path("markComplete/<int:workout_id>/", views.markComplete, name="markComplete"),
    
]