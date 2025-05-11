"""
DTOs (Data Transfer Objects) para rotinas.
Estes objetos são usados para transferir dados entre as camadas de aplicação e apresentação.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict, Any


@dataclass
class RoutineSetDTO:
    """DTO para representar um conjunto de exercícios em uma rotina."""
    id: str
    reps: Optional[int] = None
    weight: Optional[float] = None
    duration: Optional[int] = None
    distance: Optional[float] = None
    rest_seconds: Optional[int] = None


@dataclass
class RoutineExerciseDTO:
    """DTO para representar um exercício em uma rotina."""
    id: str
    exercise_template_id: str
    name: str
    notes: Optional[str] = None
    sets: List[RoutineSetDTO] = field(default_factory=list)
    order: int = 0


@dataclass
class RoutineDTO:
    """DTO para representar uma rotina completa."""
    id: str
    name: str
    exercises: List[RoutineExerciseDTO] = field(default_factory=list)
    notes: Optional[str] = None
    folder_id: Optional[str] = None
    is_public: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'RoutineDTO':
        """
        Cria uma instância de RoutineDTO a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados da rotina
            
        Returns:
            Uma nova instância de RoutineDTO
        """
        exercise_dtos = []
        for exercise_data in data.get('exercises', []):
            set_dtos = []
            for set_data in exercise_data.get('sets', []):
                set_dtos.append(RoutineSetDTO(
                    id=set_data.get('id', ''),
                    reps=set_data.get('reps'),
                    weight=set_data.get('weight'),
                    duration=set_data.get('duration'),
                    distance=set_data.get('distance'),
                    rest_seconds=set_data.get('rest_seconds')
                ))
            
            exercise_dtos.append(RoutineExerciseDTO(
                id=exercise_data.get('id', ''),
                exercise_template_id=exercise_data.get('exercise_template_id', ''),
                name=exercise_data.get('name', ''),
                notes=exercise_data.get('notes'),
                sets=set_dtos,
                order=exercise_data.get('order', 0)
            ))
                
        created_at = None
        if data.get('created_at'):
            try:
                created_at = datetime.fromisoformat(data.get('created_at'))
            except ValueError:
                pass
                
        updated_at = None
        if data.get('updated_at'):
            try:
                updated_at = datetime.fromisoformat(data.get('updated_at'))
            except ValueError:
                pass
        
        return cls(
            id=data.get('id', ''),
            name=data.get('name', ''),
            exercises=exercise_dtos,
            notes=data.get('notes'),
            folder_id=data.get('folder_id'),
            is_public=data.get('is_public', False),
            created_at=created_at,
            updated_at=updated_at
        )