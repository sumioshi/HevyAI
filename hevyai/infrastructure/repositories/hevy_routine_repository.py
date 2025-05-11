"""
Implementação do repositório de rotinas usando a API do Hevy.
"""

from typing import List, Optional, Dict, Any

from hevyai.domain.entities.routine import Routine, RoutineExercise, RoutineSet
from hevyai.domain.repositories.routine_repository import RoutineRepository
from hevyai.infrastructure.api.clients.hevy_client import HevyApiClient


class HevyRoutineRepository(RoutineRepository):
    """
    Implementação concreta do repositório de rotinas usando a API do Hevy.
    
    Esta classe implementa a interface RoutineRepository e usa o cliente da
    API do Hevy para buscar e manipular dados de rotinas.
    """
    
    def __init__(self, api_client: Optional[HevyApiClient] = None):
        """
        Inicializa o repositório com um cliente da API do Hevy.
        
        Args:
            api_client: Cliente da API do Hevy (opcional). Se não for fornecido,
                        um novo cliente será criado.
        """
        self.api_client = api_client or HevyApiClient()
    
    def get_all(self, page: int = 1, per_page: int = 10) -> List[Routine]:
        """
        Obtém uma lista paginada de rotinas da API do Hevy.
        
        Args:
            page: Número da página (padrão: 1)
            per_page: Quantidade de itens por página (padrão: 10)
            
        Returns:
            Uma lista de rotinas
        """
        response = self.api_client.get_routines(page, per_page)
        routines = []
        
        for routine_data in response.get('routines', []):
            routine = self._map_routine_from_api(routine_data)
            routines.append(routine)
            
        return routines
    
    def get_by_id(self, routine_id: str) -> Optional[Routine]:
        """
        Obtém uma rotina pelo seu ID da API do Hevy.
        
        Args:
            routine_id: ID da rotina
            
        Returns:
            A rotina encontrada ou None se não existir
        """
        try:
            response = self.api_client.get_routine(routine_id)
            return self._map_routine_from_api(response)
        except Exception as e:
            print(f"Erro ao buscar rotina por ID: {e}")
            return None
    
    def save(self, routine: Routine) -> Routine:
        """
        Salva uma rotina nova ou atualiza uma existente na API do Hevy.
        
        Args:
            routine: Rotina a ser salva
            
        Returns:
            A rotina salva
        """
        routine_data = self._map_routine_to_api(routine)
        
        if not routine.id:
            # Criar nova rotina
            response = self.api_client.create_routine(routine_data)
            return self._map_routine_from_api(response)
        else:
            # Atualizar rotina existente
            response = self.api_client.update_routine(routine.id, routine_data)
            return self._map_routine_from_api(response)
    
    def delete(self, routine_id: str) -> bool:
        """
        Exclui uma rotina pelo seu ID na API do Hevy.
        
        Args:
            routine_id: ID da rotina a ser excluída
            
        Returns:
            True se a rotina foi excluída com sucesso, False caso contrário
            
        Note:
            A API do Hevy pode não suportar exclusão direta de rotinas.
            Precisamos verificar se isso realmente é possível.
        """
        # TODO: Verificar se a API do Hevy suporta exclusão de rotinas
        # Por enquanto, retornamos False
        return False
    
    def _map_routine_from_api(self, data: Dict[str, Any]) -> Routine:
        """
        Converte dados de rotina da API do Hevy para uma entidade Routine.
        
        Args:
            data: Dados da rotina da API
            
        Returns:
            Entidade Routine
        """
        exercises = []
        
        for exercise_data in data.get('exercises', []):
            sets = []
            
            for set_data in exercise_data.get('sets', []):
                set_item = RoutineSet(
                    id=set_data.get('id', ''),
                    reps=set_data.get('reps'),
                    weight=set_data.get('weight'),
                    duration=set_data.get('duration'),
                    distance=set_data.get('distance'),
                    rest_seconds=set_data.get('rest_seconds')
                )
                sets.append(set_item)
            
            exercise = RoutineExercise(
                id=exercise_data.get('id', ''),
                exercise_template_id=exercise_data.get('exercise_template_id', ''),
                name=exercise_data.get('title', ''),  # API usa 'title' em vez de 'name'
                notes=exercise_data.get('notes'),
                sets=sets,
                order=exercise_data.get('index', 0)  # API usa 'index' em vez de 'order'
            )
            exercises.append(exercise)
        
        return Routine(
            id=data.get('id', ''),
            name=data.get('title', ''),  # API usa 'title' em vez de 'name'
            exercises=exercises,
            notes=data.get('description'),  # API usa 'description' em vez de 'notes'
            folder_id=data.get('folder_id'),
            is_public=data.get('is_public', False),
            created_at=data.get('created_at'),
            updated_at=data.get('updated_at')
        )
    
    def _map_routine_to_api(self, routine: Routine) -> Dict[str, Any]:
        """
        Converte uma entidade Routine para o formato esperado pela API do Hevy.
        
        Args:
            routine: Entidade Routine
            
        Returns:
            Dicionário no formato esperado pela API
        """
        exercises_data = []
        
        for i, exercise in enumerate(routine.exercises):
            sets_data = []
            
            for j, set_item in enumerate(exercise.sets):
                set_data = {
                    'index': j,
                    'reps': set_item.reps,
                    'weight': set_item.weight,
                    'duration': set_item.duration,
                    'distance': set_item.distance,
                    'rest_seconds': set_item.rest_seconds
                }
                sets_data.append(set_data)
            
            exercise_data = {
                'index': exercise.order if exercise.order is not None else i,
                'title': exercise.name,
                'notes': exercise.notes,
                'exercise_template_id': exercise.exercise_template_id,
                'sets': sets_data
            }
            exercises_data.append(exercise_data)
        
        return {
            'title': routine.name,
            'description': routine.notes,
            'folder_id': routine.folder_id,
            'is_public': routine.is_public,
            'exercises': exercises_data
        }