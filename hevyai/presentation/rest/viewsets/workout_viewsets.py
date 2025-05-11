"""
Viewsets para os endpoints relacionados a treinos.
"""

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from hevyai.application.use_cases.workout_use_cases import GetWorkoutsUseCase, GetWorkoutByIdUseCase
from hevyai.infrastructure.repositories.hevy_workout_repository import HevyWorkoutRepository
from hevyai.presentation.rest.serializers.workout_serializers import WorkoutSerializer


class WorkoutViewSet(viewsets.ViewSet):
    """
    Viewset para gerenciar treinos.
    
    Fornece endpoints para listar, visualizar, criar, atualizar e excluir treinos.
    """
    
    def __init__(self, **kwargs):
        """
        Inicializa o viewset com os casos de uso necessários.
        """
        super().__init__(**kwargs)
        self.workout_repository = HevyWorkoutRepository()
        self.get_workouts_use_case = GetWorkoutsUseCase(self.workout_repository)
        self.get_workout_by_id_use_case = GetWorkoutByIdUseCase(self.workout_repository)

    def list(self, request):
        """
        Lista todos os treinos de forma paginada.
        
        GET /api/workouts/
        
        Parâmetros de consulta:
        - page: Número da página (padrão: 1)
        - per_page: Itens por página (padrão: 10)
        """
        page = int(request.query_params.get('page', 1))
        per_page = int(request.query_params.get('per_page', 10))
        
        workouts = self.get_workouts_use_case.execute(page, per_page)
        serializer = WorkoutSerializer(workouts, many=True)
        
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """
        Obtém os detalhes de um treino específico.
        
        GET /api/workouts/{id}/
        """
        workout = self.get_workout_by_id_use_case.execute(pk)
        
        if not workout:
            return Response(
                {"message": "Treino não encontrado"},
                status=status.HTTP_404_NOT_FOUND
            )
            
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def count(self, request):
        """
        Obtém o número total de treinos.
        
        GET /api/workouts/count/
        """
        count = self.workout_repository.get_count()
        return Response({"count": count})