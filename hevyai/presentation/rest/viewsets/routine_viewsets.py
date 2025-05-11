"""
Viewsets para os endpoints relacionados a rotinas.
"""

from rest_framework import viewsets, status
from rest_framework.response import Response

from hevyai.application.use_cases.routine_use_cases import GetRoutinesUseCase, GetRoutineByIdUseCase
from hevyai.infrastructure.repositories.hevy_routine_repository import HevyRoutineRepository
from hevyai.presentation.rest.serializers.routine_serializers import RoutineSerializer


class RoutineViewSet(viewsets.ViewSet):
    """
    Viewset para gerenciar rotinas.
    
    Fornece endpoints para listar, visualizar, criar, atualizar e excluir rotinas.
    """
    
    def __init__(self, **kwargs):
        """
        Inicializa o viewset com os casos de uso necessários.
        """
        super().__init__(**kwargs)
        self.routine_repository = HevyRoutineRepository()
        self.get_routines_use_case = GetRoutinesUseCase(self.routine_repository)
        self.get_routine_by_id_use_case = GetRoutineByIdUseCase(self.routine_repository)

    def list(self, request):
        """
        Lista todas as rotinas de forma paginada.
        
        GET /api/routines/
        
        Parâmetros de consulta:
        - page: Número da página (padrão: 1)
        - per_page: Itens por página (padrão: 10)
        """
        page = int(request.query_params.get('page', 1))
        per_page = int(request.query_params.get('per_page', 10))
        
        routines = self.get_routines_use_case.execute(page, per_page)
        serializer = RoutineSerializer(routines, many=True)
        
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """
        Obtém os detalhes de uma rotina específica.
        
        GET /api/routines/{id}/
        """
        routine = self.get_routine_by_id_use_case.execute(pk)
        
        if not routine:
            return Response(
                {"message": "Rotina não encontrada"},
                status=status.HTTP_404_NOT_FOUND
            )
            
        serializer = RoutineSerializer(routine)
        return Response(serializer.data)