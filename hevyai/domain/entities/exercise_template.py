"""
Entidades relacionadas a modelos de exercícios no domínio da aplicação.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict, Any


@dataclass
class MuscleGroup:
    """Representa um grupo muscular associado a um exercício."""
    id: str
    name: str


@dataclass
class ExerciseTemplate:
    """
    Representa um modelo de exercício.
    
    Um modelo de exercício é uma definição de um exercício que pode ser usado
    em múltiplos treinos ou rotinas.
    """
    id: str
    name: str
    description: Optional[str] = None
    is_custom: bool = False
    muscle_groups: List[MuscleGroup] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ExerciseTemplate':
        """
        Cria uma instância de ExerciseTemplate a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do modelo de exercício
            
        Returns:
            Uma nova instância de ExerciseTemplate
        """
        muscle_groups = []
        for mg_data in data.get('muscle_groups', []):
            muscle_groups.append(MuscleGroup(
                id=mg_data.get('id', ''),
                name=mg_data.get('name', '')
            ))
            
        return cls(
            id=data.get('id', ''),
            name=data.get('name', ''),
            description=data.get('description'),
            is_custom=data.get('is_custom', False),
            muscle_groups=muscle_groups,
            created_at=datetime.fromisoformat(data.get('created_at', datetime.now().isoformat())),
            updated_at=datetime.fromisoformat(data.get('updated_at', datetime.now().isoformat()))
        )