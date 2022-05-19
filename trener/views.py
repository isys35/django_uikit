from django.shortcuts import render
from django.views.generic import ListView

from trener.models import Exercise


class ExercisesView(ListView):
    model = Exercise
    template_name = 'exercise/list.html'
