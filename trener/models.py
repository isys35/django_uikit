from django.db import models

from core.models import User


class DateTimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ExerciseBase(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Exercise(DateTimeMixin, ExerciseBase):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class UserExercise(DateTimeMixin, ExerciseBase):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Exercises(models.Model):
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    user_exercise = models.ForeignKey(
        UserExercise,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    workout = models.ForeignKey(
        'Workout',
        on_delete=models.CASCADE,
        related_name='exercise_workout'
    )

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(exercise__isnull=False) or models.Q(user_exercise__isnull=False),
                                   name='exercise_not_null'),
        ]


class Workout(DateTimeMixin, models.Model):
    exercises = models.ManyToManyField(Exercise, through=Exercises)
