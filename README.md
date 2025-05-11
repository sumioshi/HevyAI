# HevyAI

Aplicação para consumir e gerenciar dados da API do Hevy utilizando Django, DRF, React e TailwindCSS.

## Sobre o Projeto

HevyAI é uma aplicação que consome a API oficial do [Hevy](https://hevy.com/), uma plataforma para acompanhamento de treinos. A aplicação utiliza uma arquitetura DDD (Domain-Driven Design) com Django, oferecendo uma API REST com o Django Rest Framework para o backend e uma interface moderna em React com TailwindCSS para o frontend.

## Tecnologias Utilizadas

- **Backend:**
  - Python 3.10+
  - Django 4.2+
  - Django Rest Framework
  - Poetry (gerenciamento de dependências)
  - Postgres (banco de dados)

- **Frontend:**
  - React 18
  - TypeScript
  - TailwindCSS
  - Axios (requisições HTTP)

- **Infraestrutura:**
  - Docker
  - Docker Compose

## Requisitos

- Python 3.10+
- Poetry
- Node.js 18+
- Docker e Docker Compose
- Conta Hevy Pro (para obter a API key)

## Configuração Inicial

1. Clone este repositório
2. Configure o ambiente:

```bash
# Criar o arquivo .env com as configurações necessárias
cp .env.example .env
# Edite o arquivo .env e adicione sua chave de API do Hevy
```

3. Inicie os containers com Docker Compose:

```bash
docker-compose up -d
```

4. A aplicação estará disponível em:
   - Backend: http://localhost:8000
   - Frontend: http://localhost:3000

## Estrutura do Projeto

A aplicação segue uma arquitetura DDD (Domain-Driven Design) adaptada para o Django. Veja mais detalhes no arquivo [PLANNING.md](PLANNING.md).

## API Hevy

Esta aplicação consome a API oficial do Hevy, que requer uma conta Hevy Pro. Para obter sua chave de API, acesse:

- [Hevy Developer Settings](https://hevy.com/settings?developer)

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

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.