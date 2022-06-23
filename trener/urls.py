from django.urls import path

from trener import views

app_name = 'trener'

urlpatterns = [
    path('exercises', views.ExercisesView.as_view(), name='exercises'),
    path('exercises/<int:pk>', views.ExerciseDetail.as_view(), name='exercise-detail'),
    path('exercises/run/<int:pk>', views.ExerciseRun.as_view(), name='exercise-run'),
    path('create', views.ExerciseCreate.as_view(), name='create-exercise'),
]