"""
Configuração de URLs para a API REST.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from hevyai.presentation.rest.viewsets.workout_viewsets import WorkoutViewSet
from hevyai.presentation.rest.viewsets.routine_viewsets import RoutineViewSet
from hevyai.presentation.rest.viewsets.exercise_template_viewsets import ExerciseTemplateViewSet

# Criar um router e registrar os viewsets
router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'routines', RoutineViewSet, basename='routine')
router.register(r'exercise-templates', ExerciseTemplateViewSet, basename='exercise-template')

urlpatterns = [
    path('', include(router.urls)),
]