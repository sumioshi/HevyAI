"""
Casos de uso relacionados a modelos de exercícios.
Implementa as operações de negócio envolvendo modelos de exercícios.
"""

from typing import List, Optional

from hevyai.application.dtos.exercise_template_dto import ExerciseTemplateDTO
from hevyai.domain.entities.exercise_template import ExerciseTemplate
from hevyai.domain.repositories.exercise_template_repository import ExerciseTemplateRepository


class GetExerciseTemplatesUseCase:
    """Caso de uso para listar modelos de exercícios."""
    
    def __init__(self, template_repository: ExerciseTemplateRepository):
        """
        Inicializa o caso de uso com um repositório de modelos de exercícios.
        
        Args:
            template_repository: Repositório de modelos de exercícios
        """
        self.template_repository = template_repository
    
    def execute(self, page: int = 1, per_page: int = 10) -> List[ExerciseTemplateDTO]:
        """
        Executa o caso de uso para listar modelos de exercícios.
        
        Args:
            page: Número da página (padrão: 1)
            per_page: Quantidade de itens por página (padrão: 10)
            
        Returns:
            Lista de DTOs de modelos de exercícios
        """
        templates = self.template_repository.get_all(page, per_page)
        
        # Converter entidades de domínio para DTOs
        template_dtos = []
        for template in templates:
            # Converter para dict e usar o método from_dict do DTO
            template_dict = {
                "id": template.id,
                "name": template.name,
                "description": template.description,
                "is_custom": template.is_custom,
                "created_at": template.created_at.isoformat() if template.created_at else None,
                "updated_at": template.updated_at.isoformat() if template.updated_at else None,
                "muscle_groups": []
            }
            
            for mg in template.muscle_groups:
                mg_dict = {
                    "id": mg.id,
                    "name": mg.name
                }
                template_dict["muscle_groups"].append(mg_dict)
            
            template_dtos.append(ExerciseTemplateDTO.from_dict(template_dict))
        
        return template_dtos


class GetExerciseTemplateByIdUseCase:
    """Caso de uso para obter um modelo de exercício pelo ID."""
    
    def __init__(self, template_repository: ExerciseTemplateRepository):
        """
        Inicializa o caso de uso com um repositório de modelos de exercícios.
        
        Args:
            template_repository: Repositório de modelos de exercícios
        """
        self.template_repository = template_repository
    
    def execute(self, template_id: str) -> Optional[ExerciseTemplateDTO]:
        """
        Executa o caso de uso para obter um modelo de exercício pelo ID.
        
        Args:
            template_id: ID do modelo de exercício
            
        Returns:
            DTO do modelo de exercício ou None se não existir
        """
        template = self.template_repository.get_by_id(template_id)
        
        if not template:
            return None
        
        # Converter entidade de domínio para DTO
        template_dict = {
            "id": template.id,
            "name": template.name,
            "description": template.description,
            "is_custom": template.is_custom,
            "created_at": template.created_at.isoformat() if template.created_at else None,
            "updated_at": template.updated_at.isoformat() if template.updated_at else None,
            "muscle_groups": []
        }
        
        for mg in template.muscle_groups:
            mg_dict = {
                "id": mg.id,
                "name": mg.name
            }
            template_dict["muscle_groups"].append(mg_dict)
        
        return ExerciseTemplateDTO.from_dict(template_dict)