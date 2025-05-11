"""
Interface do repositório de rotinas.
Define o contrato para acesso e persistência de rotinas.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from hevyai.domain.entities.routine import Routine


class RoutineRepository(ABC):
    """
    Interface para o repositório de rotinas.
    
    Esta interface define o contrato que qualquer implementação de repositório de rotinas
    deve seguir. Os métodos definidos aqui representam as operações básicas de
    Create, Read, Update, Delete (CRUD) para a entidade Routine.
    """
    
    @abstractmethod
    def get_all(self, page: int = 1, per_page: int = 10) -> List[Routine]:
        """
        Obtém uma lista paginada de rotinas.
        
        Args:
            page: Número da página (padrão: 1)
            per_page: Quantidade de itens por página (padrão: 10)
            
        Returns:
            Uma lista de rotinas
        """
        pass
    
    @abstractmethod
    def get_by_id(self, routine_id: str) -> Optional[Routine]:
        """
        Obtém uma rotina pelo seu ID.
        
        Args:
            routine_id: ID da rotina
            
        Returns:
            A rotina encontrada ou None se não existir
        """
        pass
    
    @abstractmethod
    def save(self, routine: Routine) -> Routine:
        """
        Salva uma rotina nova ou atualiza uma existente.
        
        Args:
            routine: Rotina a ser salva
            
        Returns:
            A rotina salva
        """
        pass
    
    @abstractmethod
    def delete(self, routine_id: str) -> bool:
        """
        Exclui uma rotina pelo seu ID.
        
        Args:
            routine_id: ID da rotina a ser excluída
            
        Returns:
            True se a rotina foi excluída com sucesso, False caso contrário
        """
        pass