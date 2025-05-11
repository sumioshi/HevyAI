# HevyAI

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue" alt="Python 3.10" />
  <img src="https://img.shields.io/badge/Django-4.2-green" alt="Django 4.2" />
  <img src="https://img.shields.io/badge/React-18-blue" alt="React 18" />
  <img src="https://img.shields.io/badge/TailwindCSS-3.3-purple" alt="TailwindCSS 3.3" />
</div>

## Sobre o Projeto

HevyAI é uma aplicação para integração com a API do Hevy, desenvolvida usando Django, Django Rest Framework (DRF), React e TailwindCSS. O projeto segue os princípios de Domain-Driven Design (DDD) para garantir uma arquitetura limpa e escalável.

A aplicação permite visualizar e gerenciar dados de treinos, rotinas e exercícios através da API do Hevy, com uma interface amigável e responsiva.

## Arquitetura

O projeto segue a arquitetura Domain-Driven Design (DDD) com a seguinte estrutura:

- **Camada de Domínio**: Contém as entidades, modelos de domínio e regras de negócio
- **Camada de Aplicação**: Contém casos de uso e serviços que orquestram o domínio
- **Camada de Infraestrutura**: Contém implementações concretas como repositórios, clientes de API, etc.
- **Camada de Apresentação**: Contém a API REST (Django) e o frontend (React)

## Tecnologias Utilizadas

### Backend
- Python 3.10+
- Django 4.2+
- Django REST Framework 3.14
- Poetry (gerenciamento de dependências)
- PostgreSQL 14
- Docker e Docker Compose

### Frontend
- React 18
- TypeScript
- TailwindCSS
- Axios

## Requisitos

- Python 3.10+
- Poetry
- Node.js 18+
- Docker e Docker Compose
- Conta Hevy Pro (para obter a API key)

## Configuração do Ambiente

### Instalação e Execução

1. Clone o repositório:
```bash
git clone https://github.com/sumioshi/HevyAI.git
cd HevyAI
```

2. Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```
HEVY_API_KEY=sua_chave_api_aqui
HEVY_API_URL=https://api.hevyapp.com
DEBUG=1
SECRET_KEY=chave_secreta_django_aqui
```

3. Execute os containers Docker:
```bash
docker compose up
```

4. Acesse o backend em: `http://localhost:8000`
5. Acesse o frontend em: `http://localhost:3000` (quando estiver configurado)

## Desenvolvimento

### Comandos úteis

```bash
# Executar migrações do Django
docker-compose exec web python manage.py migrate

# Criar superusuário do Django
docker-compose exec web python manage.py createsuperuser

# Verificar logs
docker-compose logs -f web
docker-compose logs -f frontend
```

## Documentação

A documentação detalhada do projeto está disponível na pasta `docs`:

- [Planejamento do Projeto](docs/PLANNING.md)
- [Lista de Tarefas](docs/TASK.md)

## Testes

Execute os testes com o seguinte comando:

```bash
docker compose exec web python manage.py test
```

## Contribuição

Contribuições são bem-vindas! Por favor, leia o [guia de contribuição](docs/CONTRIBUTING.md) antes de enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.