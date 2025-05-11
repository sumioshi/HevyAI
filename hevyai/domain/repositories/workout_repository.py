"""
Interface do repositório de treinos.
Define o contrato para acesso e persistência de treinos.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from hevyai.domain.entities.workout import Workout


class WorkoutRepository(ABC):
    """
    Interface para o repositório de treinos.
    
    Esta interface define o contrato que qualquer implementação de repositório de treinos
    deve seguir. Os métodos definidos aqui representam as operações básicas de
    Create, Read, Update, Delete (CRUD) para a entidade Workout.
    """
    
    @abstractmethod
    def get_all(self, page: int = 1, per_page: int = 10) -> List[Workout]:
        """
        Obtém uma lista paginada de treinos.
        
        Args:
            page: Número da página (padrão: 1)
            per_page: Quantidade de itens por página (padrão: 10)
            
        Returns:
            Uma lista de treinos
        """
        pass
    
    @abstractmethod
    def get_by_id(self, workout_id: str) -> Optional[Workout]:
        """
        Obtém um treino pelo seu ID.
        
        Args:
            workout_id: ID do treino
            
        Returns:
            O treino encontrado ou None se não existir
        """
        pass
    
    @abstractmethod
    def get_count(self) -> int:
        """
        Obtém o número total de treinos.
        
        Returns:
            Número total de treinos
        """
        pass
    
    @abstractmethod
    def save(self, workout: Workout) -> Workout:
        """
        Salva um treino novo ou atualiza um existente.
        
        Args:
            workout: Treino a ser salvo
            
        Returns:
            O treino salvo
        """
        pass
    
    @abstractmethod
    def delete(self, workout_id: str) -> bool:
        """
        Exclui um treino pelo seu ID.
        
        Args:
            workout_id: ID do treino a ser excluído
            
        Returns:
            True se o treino foi excluído com sucesso, False caso contrário
        """
        pass