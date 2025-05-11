"""
Implementação do repositório de modelos de exercícios usando a API do Hevy.
"""

from typing import List, Optional, Dict, Any

from hevyai.domain.entities.exercise_template import ExerciseTemplate, MuscleGroup
from hevyai.domain.repositories.exercise_template_repository import ExerciseTemplateRepository
from hevyai.infrastructure.api.clients.hevy_client import HevyApiClient


class HevyExerciseTemplateRepository(ExerciseTemplateRepository):
    """
    Implementação concreta do repositório de modelos de exercícios usando a API do Hevy.
    
    Esta classe implementa a interface ExerciseTemplateRepository e usa o cliente da
    API do Hevy para buscar dados de modelos de exercícios.
    """
    
    def __init__(self, api_client: Optional[HevyApiClient] = None):
        """
        Inicializa o repositório com um cliente da API do Hevy.
        
        Args:
            api_client: Cliente da API do Hevy (opcional). Se não for fornecido,
                        um novo cliente será criado.
        """
        self.api_client = api_client or HevyApiClient()
    
    def get_all(self, page: int = 1, per_page: int = 10) -> List[ExerciseTemplate]:
        """
        Obtém uma lista paginada de modelos de exercícios da API do Hevy.
        
        Args:
            page: Número da página (padrão: 1)
            per_page: Quantidade de itens por página (padrão: 10)
            
        Returns:
            Uma lista de modelos de exercícios
        """
        response = self.api_client.get_exercise_templates(page, per_page)
        templates = []
        
        for template_data in response.get('exercise_templates', []):
            template = self._map_template_from_api(template_data)
            templates.append(template)
            
        return templates
    
    def get_by_id(self, template_id: str) -> Optional[ExerciseTemplate]:
        """
        Obtém um modelo de exercício pelo seu ID da API do Hevy.
        
        Args:
            template_id: ID do modelo de exercício
            
        Returns:
            O modelo de exercício encontrado ou None se não existir
        """
        try:
            response = self.api_client.get_exercise_template(template_id)
            return self._map_template_from_api(response)
        except Exception as e:
            print(f"Erro ao buscar modelo de exercício por ID: {e}")
            return None
    
    def save(self, template: ExerciseTemplate) -> ExerciseTemplate:
        """
        Salva um modelo de exercício novo ou atualiza um existente.
        
        Note: A API do Hevy pode não permitir a criação ou atualização de modelos de exercícios.
        Esta implementação é um esboço caso isso seja possível no futuro.
        
        Args:
            template: Modelo de exercício a ser salvo
            
        Returns:
            O modelo de exercício salvo
        """
        # A API do Hevy provavelmente não suporta a criação ou atualização de modelos de exercícios
        # Esta implementação é apenas um esboço
        return template
    
    def delete(self, template_id: str) -> bool:
        """
        Exclui um modelo de exercício pelo seu ID.
        
        Note: A API do Hevy pode não permitir a exclusão de modelos de exercícios.
        Esta implementação é um esboço caso isso seja possível no futuro.
        
        Args:
            template_id: ID do modelo de exercício a ser excluído
            
        Returns:
            True se o modelo de exercício foi excluído com sucesso, False caso contrário
        """
        # A API do Hevy provavelmente não suporta a exclusão de modelos de exercícios
        return False
    
    def _map_template_from_api(self, data: Dict[str, Any]) -> ExerciseTemplate:
        """
        Converte dados de modelo de exercício da API do Hevy para uma entidade ExerciseTemplate.
        
        Args:
            data: Dados do modelo de exercício da API
            
        Returns:
            Entidade ExerciseTemplate
        """
        muscle_groups = []
        
        for mg_data in data.get('muscle_groups', []):
            muscle_group = MuscleGroup(
                id=mg_data.get('id', ''),
                name=mg_data.get('name', '')
            )
            muscle_groups.append(muscle_group)
        
        return ExerciseTemplate(
            id=data.get('id', ''),
            name=data.get('name', ''),
            description=data.get('description'),
            is_custom=data.get('is_custom', False),
            muscle_groups=muscle_groups,
            created_at=data.get('created_at'),
            updated_at=data.get('updated_at')
        )