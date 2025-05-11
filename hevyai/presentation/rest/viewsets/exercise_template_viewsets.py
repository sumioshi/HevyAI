"""
Viewsets para os endpoints relacionados a modelos de exercícios.
"""

from rest_framework import viewsets, status
from rest_framework.response import Response

from hevyai.application.use_cases.exercise_template_use_cases import (
    GetExerciseTemplatesUseCase, 
    GetExerciseTemplateByIdUseCase
)
from hevyai.infrastructure.repositories.hevy_exercise_template_repository import HevyExerciseTemplateRepository
from hevyai.presentation.rest.serializers.exercise_template_serializers import ExerciseTemplateSerializer


class ExerciseTemplateViewSet(viewsets.ViewSet):
    """
    Viewset para gerenciar modelos de exercícios.
    
    Fornece endpoints para listar e visualizar modelos de exercícios.
    """
    
    def __init__(self, **kwargs):
        """
        Inicializa o viewset com os casos de uso necessários.
        """
        super().__init__(**kwargs)
        self.template_repository = HevyExerciseTemplateRepository()
        self.get_templates_use_case = GetExerciseTemplatesUseCase(self.template_repository)
        self.get_template_by_id_use_case = GetExerciseTemplateByIdUseCase(self.template_repository)

    def list(self, request):
        """
        Lista todos os modelos de exercícios de forma paginada.
        
        GET /api/exercise-templates/
        
        Parâmetros de consulta:
        - page: Número da página (padrão: 1)
        - per_page: Itens por página (padrão: 10)
        """
        page = int(request.query_params.get('page', 1))
        per_page = int(request.query_params.get('per_page', 10))
        
        templates = self.get_templates_use_case.execute(page, per_page)
        serializer = ExerciseTemplateSerializer(templates, many=True)
        
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """
        Obtém os detalhes de um modelo de exercício específico.
        
        GET /api/exercise-templates/{id}/
        """
        template = self.get_template_by_id_use_case.execute(pk)
        
        if not template:
            return Response(
                {"message": "Modelo de exercício não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
            
        serializer = ExerciseTemplateSerializer(template)
        return Response(serializer.data)