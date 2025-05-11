"""
Casos de uso relacionados a treinos.
Implementa as operações de negócio envolvendo treinos.
"""

from typing import List, Optional

from hevyai.application.dtos.workout_dto import WorkoutDTO
from hevyai.domain.entities.workout import Workout
from hevyai.domain.repositories.workout_repository import WorkoutRepository


class GetWorkoutsUseCase:
    """Caso de uso para listar treinos."""
    
    def __init__(self, workout_repository: WorkoutRepository):
        """
        Inicializa o caso de uso com um repositório de treinos.
        
        Args:
            workout_repository: Repositório de treinos
        """
        self.workout_repository = workout_repository
    
    def execute(self, page: int = 1, per_page: int = 10) -> List[WorkoutDTO]:
        """
        Executa o caso de uso para listar treinos.
        
        Args:
            page: Número da página (padrão: 1)
            per_page: Quantidade de itens por página (padrão: 10)
            
        Returns:
            Lista de DTOs de treinos
        """
        workouts = self.workout_repository.get_all(page, per_page)
        
        # Converter entidades de domínio para DTOs
        workout_dtos = []
        for workout in workouts:
            # Aqui, idealmente, você teria um método específico para converter
            # entidade para DTO. Para simplificar, estamos convertendo para dict
            # e usando o método from_dict do DTO.
            workout_dict = {
                "id": workout.id,
                "name": workout.name,
                "notes": workout.notes,
                "start_time": workout.start_time.isoformat() if workout.start_time else None,
                "end_time": workout.end_time.isoformat() if workout.end_time else None,
                "created_at": workout.created_at.isoformat() if workout.created_at else None,
                "updated_at": workout.updated_at.isoformat() if workout.updated_at else None,
                "exercises": []
            }
            
            for exercise in workout.exercises:
                exercise_dict = {
                    "id": exercise.id,
                    "exercise_template_id": exercise.exercise_template_id,
                    "name": exercise.name,
                    "notes": exercise.notes,
                    "sets": []
                }
                
                for set_item in exercise.sets:
                    set_dict = {
                        "id": set_item.id,
                        "reps": set_item.reps,
                        "weight": set_item.weight,
                        "duration": set_item.duration,
                        "distance": set_item.distance,
                        "rpe": set_item.rpe,
                        "completed": set_item.completed
                    }
                    exercise_dict["sets"].append(set_dict)
                
                workout_dict["exercises"].append(exercise_dict)
            
            workout_dtos.append(WorkoutDTO.from_dict(workout_dict))
        
        return workout_dtos


class GetWorkoutByIdUseCase:
    """Caso de uso para obter um treino pelo ID."""
    
    def __init__(self, workout_repository: WorkoutRepository):
        """
        Inicializa o caso de uso com um repositório de treinos.
        
        Args:
            workout_repository: Repositório de treinos
        """
        self.workout_repository = workout_repository
    
    def execute(self, workout_id: str) -> Optional[WorkoutDTO]:
        """
        Executa o caso de uso para obter um treino pelo ID.
        
        Args:
            workout_id: ID do treino
            
        Returns:
            DTO do treino ou None se não existir
        """
        workout = self.workout_repository.get_by_id(workout_id)
        
        if not workout:
            return None
        
        # Converter entidade de domínio para DTO (simplificado)
        workout_dict = {
            "id": workout.id,
            "name": workout.name,
            "notes": workout.notes,
            "start_time": workout.start_time.isoformat() if workout.start_time else None,
            "end_time": workout.end_time.isoformat() if workout.end_time else None,
            "created_at": workout.created_at.isoformat() if workout.created_at else None,
            "updated_at": workout.updated_at.isoformat() if workout.updated_at else None,
            "exercises": []
        }
        
        for exercise in workout.exercises:
            exercise_dict = {
                "id": exercise.id,
                "exercise_template_id": exercise.exercise_template_id,
                "name": exercise.name,
                "notes": exercise.notes,
                "sets": []
            }
            
            for set_item in exercise.sets:
                set_dict = {
                    "id": set_item.id,
                    "reps": set_item.reps,
                    "weight": set_item.weight,
                    "duration": set_item.duration,
                    "distance": set_item.distance,
                    "rpe": set_item.rpe,
                    "completed": set_item.completed
                }
                exercise_dict["sets"].append(set_dict)
            
            workout_dict["exercises"].append(exercise_dict)
        
        return WorkoutDTO.from_dict(workout_dict)