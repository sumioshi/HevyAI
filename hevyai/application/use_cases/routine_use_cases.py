"""
Casos de uso relacionados a rotinas.
Implementa as operações de negócio envolvendo rotinas.
"""

from typing import List, Optional

from hevyai.application.dtos.routine_dto import RoutineDTO
from hevyai.domain.entities.routine import Routine
from hevyai.domain.repositories.routine_repository import RoutineRepository


class GetRoutinesUseCase:
    """Caso de uso para listar rotinas."""
    
    def __init__(self, routine_repository: RoutineRepository):
        """
        Inicializa o caso de uso com um repositório de rotinas.
        
        Args:
            routine_repository: Repositório de rotinas
        """
        self.routine_repository = routine_repository
    
    def execute(self, page: int = 1, per_page: int = 10) -> List[RoutineDTO]:
        """
        Executa o caso de uso para listar rotinas.
        
        Args:
            page: Número da página (padrão: 1)
            per_page: Quantidade de itens por página (padrão: 10)
            
        Returns:
            Lista de DTOs de rotinas
        """
        routines = self.routine_repository.get_all(page, per_page)
        
        # Converter entidades de domínio para DTOs
        routine_dtos = []
        for routine in routines:
            # Aqui, idealmente, você teria um método específico para converter
            # entidade para DTO. Para simplificar, estamos convertendo para dict
            # e usando o método from_dict do DTO.
            routine_dict = {
                "id": routine.id,
                "name": routine.name,
                "notes": routine.notes,
                "folder_id": routine.folder_id,
                "is_public": routine.is_public,
                "created_at": routine.created_at.isoformat() if routine.created_at else None,
                "updated_at": routine.updated_at.isoformat() if routine.updated_at else None,
                "exercises": []
            }
            
            for exercise in routine.exercises:
                exercise_dict = {
                    "id": exercise.id,
                    "exercise_template_id": exercise.exercise_template_id,
                    "name": exercise.name,
                    "notes": exercise.notes,
                    "order": exercise.order,
                    "sets": []
                }
                
                for set_item in exercise.sets:
                    set_dict = {
                        "id": set_item.id,
                        "reps": set_item.reps,
                        "weight": set_item.weight,
                        "duration": set_item.duration,
                        "distance": set_item.distance,
                        "rest_seconds": set_item.rest_seconds
                    }
                    exercise_dict["sets"].append(set_dict)
                
                routine_dict["exercises"].append(exercise_dict)
            
            routine_dtos.append(RoutineDTO.from_dict(routine_dict))
        
        return routine_dtos


class GetRoutineByIdUseCase:
    """Caso de uso para obter uma rotina pelo ID."""
    
    def __init__(self, routine_repository: RoutineRepository):
        """
        Inicializa o caso de uso com um repositório de rotinas.
        
        Args:
            routine_repository: Repositório de rotinas
        """
        self.routine_repository = routine_repository
    
    def execute(self, routine_id: str) -> Optional[RoutineDTO]:
        """
        Executa o caso de uso para obter uma rotina pelo ID.
        
        Args:
            routine_id: ID da rotina
            
        Returns:
            DTO da rotina ou None se não existir
        """
        routine = self.routine_repository.get_by_id(routine_id)
        
        if not routine:
            return None
        
        # Converter entidade de domínio para DTO (simplificado)
        routine_dict = {
            "id": routine.id,
            "name": routine.name,
            "notes": routine.notes,
            "folder_id": routine.folder_id,
            "is_public": routine.is_public,
            "created_at": routine.created_at.isoformat() if routine.created_at else None,
            "updated_at": routine.updated_at.isoformat() if routine.updated_at else None,
            "exercises": []
        }
        
        for exercise in routine.exercises:
            exercise_dict = {
                "id": exercise.id,
                "exercise_template_id": exercise.exercise_template_id,
                "name": exercise.name,
                "notes": exercise.notes,
                "order": exercise.order,
                "sets": []
            }
            
            for set_item in exercise.sets:
                set_dict = {
                    "id": set_item.id,
                    "reps": set_item.reps,
                    "weight": set_item.weight,
                    "duration": set_item.duration,
                    "distance": set_item.distance,
                    "rest_seconds": set_item.rest_seconds
                }
                exercise_dict["sets"].append(set_dict)
            
            routine_dict["exercises"].append(exercise_dict)
        
        return RoutineDTO.from_dict(routine_dict)