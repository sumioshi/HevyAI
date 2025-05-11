"""
Interface do repositório de modelos de exercícios.
Define o contrato para acesso e persistência de modelos de exercícios.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from hevyai.domain.entities.exercise_template import ExerciseTemplate


class ExerciseTemplateRepository(ABC):
    """
    Interface para o repositório de modelos de exercícios.
    
    Esta interface define o contrato que qualquer implementação de repositório de modelos de exercícios
    deve seguir. Os métodos definidos aqui representam as operações básicas de
    Create, Read, Update, Delete (CRUD) para a entidade ExerciseTemplate.
    """
    
    @abstractmethod
    def get_all(self, page: int = 1, per_page: int = 10) -> List[ExerciseTemplate]:
        """
        Obtém uma lista paginada de modelos de exercícios.
        
        Args:
            page: Número da página (padrão: 1)
            per_page: Quantidade de itens por página (padrão: 10)
            
        Returns:
            Uma lista de modelos de exercícios
        """
        pass
    
    @abstractmethod
    def get_by_id(self, template_id: str) -> Optional[ExerciseTemplate]:
        """
        Obtém um modelo de exercício pelo seu ID.
        
        Args:
            template_id: ID do modelo de exercício
            
        Returns:
            O modelo de exercício encontrado ou None se não existir
        """
        pass
    
    @abstractmethod
    def save(self, template: ExerciseTemplate) -> ExerciseTemplate:
        """
        Salva um modelo de exercício novo ou atualiza um existente.
        
        Args:
            template: Modelo de exercício a ser salvo
            
        Returns:
            O modelo de exercício salvo
        """
        pass
    
    @abstractmethod
    def delete(self, template_id: str) -> bool:
        """
        Exclui um modelo de exercício pelo seu ID.
        
        Args:
            template_id: ID do modelo de exercício a ser excluído
            
        Returns:
            True se o modelo de exercício foi excluído com sucesso, False caso contrário
        """
        pass