from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from trener.forms import ExerciseForm
from trener.models import Exercise


class ExercisesView(ListView):
    model = Exercise
    template_name = 'exercise/list.html'


class ExerciseCreate(CreateView):
    model = Exercise
    template_name = 'exercise/create.html'
    form_class = ExerciseForm
    success_url = reverse_lazy('core:trener:exercises')


class ExerciseDetail(DetailView):
    model = Exercise
    template_name = 'exercise/detail.html'


class ExerciseRun(DetailView):
    model = Exercise
    template_name = 'exercise/run.html'
