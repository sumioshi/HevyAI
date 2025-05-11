"""
Serializadores para treinos.
Converte objetos de treino para JSON e vice-versa.
"""

from rest_framework import serializers


class SetSerializer(serializers.Serializer):
    """Serializador para um conjunto de exercícios em um treino."""
    id = serializers.CharField(read_only=True)
    reps = serializers.IntegerField(allow_null=True, required=False)
    weight = serializers.FloatField(allow_null=True, required=False)
    duration = serializers.IntegerField(allow_null=True, required=False)
    distance = serializers.FloatField(allow_null=True, required=False)
    rpe = serializers.FloatField(allow_null=True, required=False)
    completed = serializers.BooleanField(default=True)


class ExerciseSerializer(serializers.Serializer):
    """Serializador para um exercício em um treino."""
    id = serializers.CharField(read_only=True)
    exercise_template_id = serializers.CharField()
    name = serializers.CharField()
    notes = serializers.CharField(allow_null=True, required=False)
    sets = SetSerializer(many=True)


class WorkoutSerializer(serializers.Serializer):
    """Serializador para um treino completo."""
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    exercises = ExerciseSerializer(many=True)
    notes = serializers.CharField(allow_null=True, required=False)
    start_time = serializers.DateTimeField(allow_null=True, required=False)
    end_time = serializers.DateTimeField(allow_null=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)