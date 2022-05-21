from django.urls import path

from trener import views

app_name = 'trener'

urlpatterns = [
    path('', views.ExercisesView.as_view(), name='exercises'),
    path('create', views.ExerciseCreate.as_view(), name='create_exercise'),
]