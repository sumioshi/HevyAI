"""
Entidades relacionadas a rotinas no domínio da aplicação.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict, Any


@dataclass
class RoutineSet:
    """Representa um conjunto de exercícios em uma rotina."""
    id: str
    reps: Optional[int] = None
    weight: Optional[float] = None
    duration: Optional[int] = None  # duração em segundos
    distance: Optional[float] = None
    rest_seconds: Optional[int] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'RoutineSet':
        """
        Cria uma instância de RoutineSet a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do conjunto
            
        Returns:
            Uma nova instância de RoutineSet
        """
        return cls(
            id=data.get('id', ''),
            reps=data.get('reps'),
            weight=data.get('weight'),
            duration=data.get('duration'),
            distance=data.get('distance'),
            rest_seconds=data.get('rest_seconds'),
            created_at=datetime.fromisoformat(data.get('created_at', datetime.now().isoformat())),
            updated_at=datetime.fromisoformat(data.get('updated_at', datetime.now().isoformat()))
        )


@dataclass
class RoutineExercise:
    """Representa um exercício em uma rotina."""
    id: str
    exercise_template_id: str
    name: str
    notes: Optional[str] = None
    sets: List[RoutineSet] = field(default_factory=list)
    order: int = 0
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'RoutineExercise':
        """
        Cria uma instância de RoutineExercise a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do exercício
            
        Returns:
            Uma nova instância de RoutineExercise
        """
        sets = [RoutineSet.from_dict(set_data) for set_data in data.get('sets', [])]
        return cls(
            id=data.get('id', ''),
            exercise_template_id=data.get('exercise_template_id', ''),
            name=data.get('name', ''),
            notes=data.get('notes'),
            sets=sets,
            order=data.get('order', 0),
            created_at=datetime.fromisoformat(data.get('created_at', datetime.now().isoformat())),
            updated_at=datetime.fromisoformat(data.get('updated_at', datetime.now().isoformat()))
        )


@dataclass
class Routine:
    """Representa uma rotina de treino completa."""
    id: str
    name: str
    exercises: List[RoutineExercise] = field(default_factory=list)
    notes: Optional[str] = None
    folder_id: Optional[str] = None
    is_public: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Routine':
        """
        Cria uma instância de Routine a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados da rotina
            
        Returns:
            Uma nova instância de Routine
        """
        exercises = [RoutineExercise.from_dict(exercise_data) for exercise_data in data.get('exercises', [])]
                
        return cls(
            id=data.get('id', ''),
            name=data.get('name', ''),
            exercises=exercises,
            notes=data.get('notes'),
            folder_id=data.get('folder_id'),
            is_public=data.get('is_public', False),
            created_at=datetime.fromisoformat(data.get('created_at', datetime.now().isoformat())),
            updated_at=datetime.fromisoformat(data.get('updated_at', datetime.now().isoformat()))
        )