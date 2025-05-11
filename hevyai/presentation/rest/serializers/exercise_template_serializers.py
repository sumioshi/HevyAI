"""
Serializadores para modelos de exercícios.
Converte objetos de modelo de exercício para JSON e vice-versa.
"""

from rest_framework import serializers


class MuscleGroupSerializer(serializers.Serializer):
    """Serializador para um grupo muscular."""
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()


class ExerciseTemplateSerializer(serializers.Serializer):
    """Serializador para um modelo de exercício."""
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(allow_null=True, required=False)
    is_custom = serializers.BooleanField(default=False)
    muscle_groups = MuscleGroupSerializer(many=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)