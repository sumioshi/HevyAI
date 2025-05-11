"""
DTOs (Data Transfer Objects) para modelos de exercícios.
Estes objetos são usados para transferir dados entre as camadas de aplicação e apresentação.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict, Any


@dataclass
class MuscleGroupDTO:
    """DTO para representar um grupo muscular."""
    id: str
    name: str


@dataclass
class ExerciseTemplateDTO:
    """DTO para representar um modelo de exercício."""
    id: str
    name: str
    description: Optional[str] = None
    is_custom: bool = False
    muscle_groups: List[MuscleGroupDTO] = field(default_factory=list)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ExerciseTemplateDTO':
        """
        Cria uma instância de ExerciseTemplateDTO a partir de um dicionário.
        
        Args:
            data: Dicionário contendo os dados do modelo de exercício
            
        Returns:
            Uma nova instância de ExerciseTemplateDTO
        """
        muscle_group_dtos = []
        for mg_data in data.get('muscle_groups', []):
            muscle_group_dtos.append(MuscleGroupDTO(
                id=mg_data.get('id', ''),
                name=mg_data.get('name', '')
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
            description=data.get('description'),
            is_custom=data.get('is_custom', False),
            muscle_groups=muscle_group_dtos,
            created_at=created_at,
            updated_at=updated_at
        )