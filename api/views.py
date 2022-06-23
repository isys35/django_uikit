from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

from api.serializers import ExerciseSerializer


class CreateExercise(CreateAPIView):
    serializer_class = ExerciseSerializer


    def perform_create(self, serializer):
        return
