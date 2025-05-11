"""
Entidades relacionadas a treinos no domínio da aplicação.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict, Any


@dataclass
class Set:
    """Representa um conjunto de exercícios em um treino."""
    id: str
    reps: Optional[int] = None
    weight: Optional[float] = None
    duration: Optional[int] = None  # duração em segundos
    distance: Optional[float] = None
    rpe: Optional[float] = None  # Rating of Perceived Exertion
    completed: bool = True
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Set':
        """
        Cria uma instância de Set a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do conjunto
            
        Returns:
            Uma nova instância de Set
        """
        return cls(
            id=data.get('id', ''),
            reps=data.get('reps'),
            weight=data.get('weight'),
            duration=data.get('duration'),
            distance=data.get('distance'),
            rpe=data.get('rpe'),
            completed=data.get('completed', True),
            created_at=datetime.fromisoformat(data.get('created_at', datetime.now().isoformat())),
            updated_at=datetime.fromisoformat(data.get('updated_at', datetime.now().isoformat()))
        )


@dataclass
class Exercise:
    """Representa um exercício em um treino."""
    id: str
    exercise_template_id: str
    name: str
    notes: Optional[str] = None
    sets: List[Set] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Exercise':
        """
        Cria uma instância de Exercise a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do exercício
            
        Returns:
            Uma nova instância de Exercise
        """
        sets = [Set.from_dict(set_data) for set_data in data.get('sets', [])]
        return cls(
            id=data.get('id', ''),
            exercise_template_id=data.get('exercise_template_id', ''),
            name=data.get('name', ''),
            notes=data.get('notes'),
            sets=sets,
            created_at=datetime.fromisoformat(data.get('created_at', datetime.now().isoformat())),
            updated_at=datetime.fromisoformat(data.get('updated_at', datetime.now().isoformat()))
        )


@dataclass
class Workout:
    """Representa um treino completo."""
    id: str
    name: str
    exercises: List[Exercise] = field(default_factory=list)
    notes: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Workout':
        """
        Cria uma instância de Workout a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do treino
            
        Returns:
            Uma nova instância de Workout
        """
        exercises = [Exercise.from_dict(exercise_data) for exercise_data in data.get('exercises', [])]
        
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
                
        return cls(
            id=data.get('id', ''),
            name=data.get('name', ''),
            exercises=exercises,
            notes=data.get('notes'),
            start_time=start_time,
            end_time=end_time,
            created_at=datetime.fromisoformat(data.get('created_at', datetime.now().isoformat())),
            updated_at=datetime.fromisoformat(data.get('updated_at', datetime.now().isoformat()))
        )