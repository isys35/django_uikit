from django.forms import ModelForm

from trener.models import Exercise


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ['name']