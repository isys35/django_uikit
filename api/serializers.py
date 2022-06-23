from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers
from rest_framework.fields import Field

from trener.models import Exercise


class CustomField(Field):

    def to_internal_value(self, data):
        return "data"

    def to_representation(self, value):
        return "value"



class ExerciseSerializer(serializers.ModelSerializer):
    creator_id = serializers.CharField(source='creator.id')

    class Meta:
        model = Exercise
        fields = ('creator_id', 'name')
