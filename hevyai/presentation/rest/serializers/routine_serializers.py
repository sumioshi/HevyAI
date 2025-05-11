"""
Serializadores para rotinas.
Converte objetos de rotina para JSON e vice-versa.
"""

from rest_framework import serializers


class RoutineSetSerializer(serializers.Serializer):
    """Serializador para um conjunto de exercícios em uma rotina."""
    id = serializers.CharField(read_only=True)
    reps = serializers.IntegerField(allow_null=True, required=False)
    weight = serializers.FloatField(allow_null=True, required=False)
    duration = serializers.IntegerField(allow_null=True, required=False)
    distance = serializers.FloatField(allow_null=True, required=False)
    rest_seconds = serializers.IntegerField(allow_null=True, required=False)


class RoutineExerciseSerializer(serializers.Serializer):
    """Serializador para um exercício em uma rotina."""
    id = serializers.CharField(read_only=True)
    exercise_template_id = serializers.CharField()
    name = serializers.CharField()
    notes = serializers.CharField(allow_null=True, required=False)
    sets = RoutineSetSerializer(many=True)
    order = serializers.IntegerField(default=0)


class RoutineSerializer(serializers.Serializer):
    """Serializador para uma rotina completa."""
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    exercises = RoutineExerciseSerializer(many=True)
    notes = serializers.CharField(allow_null=True, required=False)
    folder_id = serializers.CharField(allow_null=True, required=False)
    is_public = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)