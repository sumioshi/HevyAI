"""
Implementação do repositório de treinos usando a API do Hevy.
"""

from typing import List, Optional, Dict, Any

from hevyai.domain.entities.workout import Workout, Exercise, Set
from hevyai.domain.repositories.workout_repository import WorkoutRepository
from hevyai.infrastructure.api.clients.hevy_client import HevyApiClient


class HevyWorkoutRepository(WorkoutRepository):
    """
    Implementação concreta do repositório de treinos usando a API do Hevy.
    
    Esta classe implementa a interface WorkoutRepository e usa o cliente da
    API do Hevy para buscar e manipular dados de treinos.
    """
    
    def __init__(self, api_client: Optional[HevyApiClient] = None):
        """
        Inicializa o repositório com um cliente da API do Hevy.
        
        Args:
            api_client: Cliente da API do Hevy (opcional). Se não for fornecido,
                        um novo cliente será criado.
        """
        self.api_client = api_client or HevyApiClient()
    
    def get_all(self, page: int = 1, per_page: int = 10) -> List[Workout]:
        """
        Obtém uma lista paginada de treinos da API do Hevy.
        
        Args:
            page: Número da página (padrão: 1)
            per_page: Quantidade de itens por página (padrão: 10)
            
        Returns:
            Uma lista de treinos
        """
        response = self.api_client.get_workouts(page, per_page)
        workouts = []
        
        for workout_data in response.get('workouts', []):
            workout = self._map_workout_from_api(workout_data)
            workouts.append(workout)
            
        return workouts
    
    def get_by_id(self, workout_id: str) -> Optional[Workout]:
        """
        Obtém um treino pelo seu ID da API do Hevy.
        
        Args:
            workout_id: ID do treino
            
        Returns:
            O treino encontrado ou None se não existir
        """
        try:
            response = self.api_client.get_workout(workout_id)
            return self._map_workout_from_api(response)
        except Exception as e:
            print(f"Erro ao buscar treino por ID: {e}")
            return None
    
    def get_count(self) -> int:
        """
        Obtém o número total de treinos da API do Hevy.
        
        Returns:
            Número total de treinos
        """
        return self.api_client.get_workout_count()
    
    def save(self, workout: Workout) -> Workout:
        """
        Salva um treino novo ou atualiza um existente na API do Hevy.
        
        Args:
            workout: Treino a ser salvo
            
        Returns:
            O treino salvo
        """
        workout_data = self._map_workout_to_api(workout)
        
        if not workout.id:
            # Criar novo treino
            response = self.api_client.create_workout(workout_data)
            return self._map_workout_from_api(response)
        else:
            # Atualizar treino existente
            response = self.api_client.update_workout(workout.id, workout_data)
            return self._map_workout_from_api(response)
    
    def delete(self, workout_id: str) -> bool:
        """
        Exclui um treino pelo seu ID na API do Hevy.
        
        Args:
            workout_id: ID do treino a ser excluído
            
        Returns:
            True se o treino foi excluído com sucesso, False caso contrário
            
        Note:
            A API do Hevy pode não suportar exclusão direta de treinos.
            Precisamos verificar se isso realmente é possível.
        """
        # TODO: Verificar se a API do Hevy suporta exclusão de treinos
        # Por enquanto, retornamos False
        return False
    
    def _map_workout_from_api(self, data: Dict[str, Any]) -> Workout:
        """
        Converte dados de treino da API do Hevy para uma entidade Workout.
        
        Args:
            data: Dados do treino da API
            
        Returns:
            Entidade Workout
        """
        exercises = []
        
        for exercise_data in data.get('exercises', []):
            sets = []
            
            for set_data in exercise_data.get('sets', []):
                set_item = Set(
                    id=set_data.get('id', ''),
                    reps=set_data.get('reps'),
                    weight=set_data.get('weight'),
                    duration=set_data.get('duration'),
                    distance=set_data.get('distance'),
                    rpe=set_data.get('rpe'),
                    completed=set_data.get('completed', True)
                )
                sets.append(set_item)
            
            exercise = Exercise(
                id=exercise_data.get('id', ''),
                exercise_template_id=exercise_data.get('exercise_template_id', ''),
                name=exercise_data.get('title', ''),  # API usa 'title' em vez de 'name'
                notes=exercise_data.get('notes'),
                sets=sets
            )
            exercises.append(exercise)
        
        return Workout(
            id=data.get('id', ''),
            name=data.get('title', ''),  # API usa 'title' em vez de 'name'
            exercises=exercises,
            notes=data.get('description'),  # API usa 'description' em vez de 'notes'
            start_time=data.get('start_time'),
            end_time=data.get('end_time'),
            created_at=data.get('created_at'),
            updated_at=data.get('updated_at')
        )
    
    def _map_workout_to_api(self, workout: Workout) -> Dict[str, Any]:
        """
        Converte uma entidade Workout para o formato esperado pela API do Hevy.
        
        Args:
            workout: Entidade Workout
            
        Returns:
            Dicionário no formato esperado pela API
        """
        exercises_data = []
        
        for i, exercise in enumerate(workout.exercises):
            sets_data = []
            
            for j, set_item in enumerate(exercise.sets):
                set_data = {
                    'index': j,
                    'type': 'normal',
                    'reps': set_item.reps,
                    'weight': set_item.weight,
                    'duration': set_item.duration,
                    'distance': set_item.distance,
                    'rpe': set_item.rpe,
                    'completed': set_item.completed
                }
                sets_data.append(set_data)
            
            exercise_data = {
                'index': i,
                'title': exercise.name,
                'notes': exercise.notes,
                'exercise_template_id': exercise.exercise_template_id,
                'supersets_id': 0,  # valor padrão
                'sets': sets_data
            }
            exercises_data.append(exercise_data)
        
        return {
            'title': workout.name,
            'description': workout.notes,
            'start_time': workout.start_time.isoformat() if workout.start_time else None,
            'end_time': workout.end_time.isoformat() if workout.end_time else None,
            'exercises': exercises_data
        }