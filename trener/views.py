from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

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