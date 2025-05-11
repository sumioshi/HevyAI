"""
DTOs (Data Transfer Objects) para treinos.
Estes objetos são usados para transferir dados entre as camadas de aplicação e apresentação.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict, Any


@dataclass
class SetDTO:
    """DTO para representar um conjunto de exercícios em um treino."""
    id: str
    reps: Optional[int] = None
    weight: Optional[float] = None
    duration: Optional[int] = None
    distance: Optional[float] = None
    rpe: Optional[float] = None
    completed: bool = True


@dataclass
class ExerciseDTO:
    """DTO para representar um exercício em um treino."""
    id: str
    exercise_template_id: str
    name: str
    notes: Optional[str] = None
    sets: List[SetDTO] = field(default_factory=list)


@dataclass
class WorkoutDTO:
    """DTO para representar um treino completo."""
    id: str
    name: str
    exercises: List[ExerciseDTO] = field(default_factory=list)
    notes: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'WorkoutDTO':
        """
        Cria uma instância de WorkoutDTO a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do treino
            
        Returns:
            Uma nova instância de WorkoutDTO
        """
        exercise_dtos = []
        for exercise_data in data.get('exercises', []):
            set_dtos = []
            for set_data in exercise_data.get('sets', []):
                set_dtos.append(SetDTO(
                    id=set_data.get('id', ''),
                    reps=set_data.get('reps'),
                    weight=set_data.get('weight'),
                    duration=set_data.get('duration'),
                    distance=set_data.get('distance'),
                    rpe=set_data.get('rpe'),
                    completed=set_data.get('completed', True)
                ))
            
            exercise_dtos.append(ExerciseDTO(
                id=exercise_data.get('id', ''),
                exercise_template_id=exercise_data.get('exercise_template_id', ''),
                name=exercise_data.get('name', ''),
                notes=exercise_data.get('notes'),
                sets=set_dtos
            ))
        
        start_time = None
        if data.get('start_time'):
            try:
                start_time = datetime.fromisoformat(data.get('start_time'))
            except ValueError:
                pass
                
        end_time = None
        if data.get('end_time'):
            try:
                end_time = datetime.fromisoformat(data.get('end_time'))
            except ValueError:
                pass
                
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
            start_time=start_time,
            end_time=end_time,
            created_at=created_at,
            updated_at=updated_at
        )