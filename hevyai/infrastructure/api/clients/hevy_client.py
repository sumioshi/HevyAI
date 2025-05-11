"""
Cliente para a API do Hevy.
Responsável por fazer requisições para a API externa do Hevy.
"""

import requests
from django.conf import settings
from typing import Dict, Any, Optional, List


class HevyApiClient:
    """Cliente para a API do Hevy."""

    def __init__(self, api_key: Optional[str] = None, api_url: Optional[str] = None):
        """
        Inicializa o cliente da API do Hevy.
        
        Args:
            api_key: Chave da API do Hevy (opcional, padrão: settings.HEVY_API_KEY)
            api_url: URL da API do Hevy (opcional, padrão: settings.HEVY_API_URL)
        """
        self.api_key = api_key or settings.HEVY_API_KEY
        self.api_url = api_url or settings.HEVY_API_URL
        self.session = requests.Session()
        self.session.headers.update({
            'api-key': self.api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })

    def get_workouts(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Obtém uma lista paginada de treinos.
        
        Args:
            page: Número da página (padrão: 1)
            page_size: Quantidade de itens por página (padrão: 10, máximo permitido pela API: 10)
            
        Returns:
            Dicionário com a resposta da API contendo página atual, total de páginas e treinos
        """
        response = self.session.get(
            f"{self.api_url}/v1/workouts",
            params={"page": page, "pageSize": min(page_size, 10)}
        )
        response.raise_for_status()
        return response.json()

    def get_workout(self, workout_id: str) -> Dict[str, Any]:
        """
        Obtém os detalhes de um treino específico.
        
        Args:
            workout_id: ID do treino
            
        Returns:
            Dicionário com a resposta da API contendo detalhes completos do treino
        """
        response = self.session.get(f"{self.api_url}/v1/workouts/{workout_id}")
        response.raise_for_status()
        return response.json()

    def get_workout_count(self) -> int:
        """
        Obtém o número total de treinos na conta.
        
        Returns:
            Número total de treinos
        """
        response = self.session.get(f"{self.api_url}/v1/workouts/count")
        response.raise_for_status()
        return response.json().get("count", 0)
    
    def create_workout(self, workout_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Cria um novo treino.
        
        Args:
            workout_data: Dados do treino a ser criado
            
        Returns:
            Dicionário com a resposta da API contendo o treino criado
        """
        response = self.session.post(
            f"{self.api_url}/v1/workouts",
            json=workout_data
        )
        response.raise_for_status()
        return response.json()
    
    def update_workout(self, workout_id: str, workout_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Atualiza um treino existente.
        
        Args:
            workout_id: ID do treino a ser atualizado
            workout_data: Novos dados do treino
            
        Returns:
            Dicionário com a resposta da API contendo o treino atualizado
        """
        response = self.session.put(
            f"{self.api_url}/v1/workouts/{workout_id}",
            json=workout_data
        )
        response.raise_for_status()
        return response.json()

    def get_workout_events(self, since_date: str, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Obtém eventos de treinos (atualizações ou exclusões) desde uma data específica.
        
        Args:
            since_date: Data ISO 8601 a partir da qual buscar eventos
            page: Número da página (padrão: 1)
            page_size: Quantidade de itens por página (padrão: 10)
            
        Returns:
            Dicionário com a resposta da API contendo eventos de treinos
        """
        response = self.session.get(
            f"{self.api_url}/v1/workouts/events",
            params={"since_date": since_date, "page": page, "pageSize": min(page_size, 10)}
        )
        response.raise_for_status()
        return response.json()

    def get_routines(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Obtém uma lista paginada de rotinas.
        
        Args:
            page: Número da página (padrão: 1)
            page_size: Quantidade de itens por página (padrão: 10)
            
        Returns:
            Dicionário com a resposta da API contendo rotinas
        """
        response = self.session.get(
            f"{self.api_url}/v1/routines",
            params={"page": page, "pageSize": min(page_size, 10)}
        )
        response.raise_for_status()
        return response.json()

    def get_routine(self, routine_id: str) -> Dict[str, Any]:
        """
        Obtém os detalhes de uma rotina específica.
        
        Args:
            routine_id: ID da rotina
            
        Returns:
            Dicionário com a resposta da API contendo detalhes da rotina
        """
        response = self.session.get(f"{self.api_url}/v1/routines/{routine_id}")
        response.raise_for_status()
        return response.json()
    
    def create_routine(self, routine_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Cria uma nova rotina.
        
        Args:
            routine_data: Dados da rotina a ser criada
            
        Returns:
            Dicionário com a resposta da API contendo a rotina criada
        """
        response = self.session.post(
            f"{self.api_url}/v1/routines",
            json=routine_data
        )
        response.raise_for_status()
        return response.json()
    
    def update_routine(self, routine_id: str, routine_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Atualiza uma rotina existente.
        
        Args:
            routine_id: ID da rotina a ser atualizada
            routine_data: Novos dados da rotina
            
        Returns:
            Dicionário com a resposta da API contendo a rotina atualizada
        """
        response = self.session.put(
            f"{self.api_url}/v1/routines/{routine_id}",
            json=routine_data
        )
        response.raise_for_status()
        return response.json()

    def get_exercise_templates(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Obtém uma lista paginada de modelos de exercícios.
        
        Args:
            page: Número da página (padrão: 1)
            page_size: Quantidade de itens por página (padrão: 10)
            
        Returns:
            Dicionário com a resposta da API contendo modelos de exercícios
        """
        response = self.session.get(
            f"{self.api_url}/v1/exercise_templates",
            params={"page": page, "pageSize": min(page_size, 10)}
        )
        response.raise_for_status()
        return response.json()

    def get_exercise_template(self, template_id: str) -> Dict[str, Any]:
        """
        Obtém os detalhes de um modelo de exercício específico.
        
        Args:
            template_id: ID do modelo de exercício
            
        Returns:
            Dicionário com a resposta da API contendo detalhes do modelo de exercício
        """
        response = self.session.get(f"{self.api_url}/v1/exercise_templates/{template_id}")
        response.raise_for_status()
        return response.json()
    
    def get_routine_folders(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Obtém uma lista paginada de pastas de rotinas.
        
        Args:
            page: Número da página (padrão: 1)
            page_size: Quantidade de itens por página (padrão: 10)
            
        Returns:
            Dicionário com a resposta da API contendo pastas de rotinas
        """
        response = self.session.get(
            f"{self.api_url}/v1/routine_folders",
            params={"page": page, "pageSize": min(page_size, 10)}
        )
        response.raise_for_status()
        return response.json()
    
    def get_routine_folder(self, folder_id: str) -> Dict[str, Any]:
        """
        Obtém os detalhes de uma pasta de rotinas específica.
        
        Args:
            folder_id: ID da pasta de rotinas
            
        Returns:
            Dicionário com a resposta da API contendo detalhes da pasta de rotinas
        """
        response = self.session.get(f"{self.api_url}/v1/routine_folders/{folder_id}")
        response.raise_for_status()
        return response.json()
    
    def create_routine_folder(self, folder_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Cria uma nova pasta de rotinas.
        
        Args:
            folder_data: Dados da pasta a ser criada
            
        Returns:
            Dicionário com a resposta da API contendo a pasta criada
        """
        response = self.session.post(
            f"{self.api_url}/v1/routine_folders",
            json=folder_data
        )
        response.raise_for_status()
        return response.json()