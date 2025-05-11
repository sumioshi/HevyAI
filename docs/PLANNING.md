# Planejamento do Projeto HevyAI

## Visão Geral da Arquitetura

O HevyAI é estruturado seguindo os princípios de **Domain-Driven Design (DDD)**, organizando o código em camadas distintas com responsabilidades bem definidas. Esta abordagem favorece a manutenção, testabilidade e evolução do sistema.

### Estrutura de Camadas

#### 1. Camada de Domínio (`hevyai/domain/`)

A camada central que contém as regras de negócio e entidades fundamentais.

- **Entidades**: Objetos com identidade e ciclo de vida (`hevyai/domain/entities/`)
  - `workout.py` - Representação de um treino
  - `routine.py` - Representação de uma rotina
  - `exercise_template.py` - Representação de um modelo de exercício

- **Repositórios (Interfaces)**: Contratos para acesso a dados (`hevyai/domain/repositories/`)
  - `workout_repository.py` - Interface para operações com treinos
  - `routine_repository.py` - Interface para operações com rotinas
  - `exercise_template_repository.py` - Interface para operações com templates de exercícios

- **Serviços de Domínio**: Lógica de negócio que opera em múltiplas entidades (`hevyai/domain/services/`)
  - `workout_analysis_service.py` - Análise de treinos e métricas

#### 2. Camada de Aplicação (`hevyai/application/`)

Orquestra os fluxos de uso do sistema, utilizando os componentes da camada de domínio.

- **Casos de Uso**: Implementam operações específicas solicitadas pela camada de apresentação
  - `workout_use_cases.py` - Operações relacionadas a treinos
  - `routine_use_cases.py` - Operações relacionadas a rotinas
  - `exercise_template_use_cases.py` - Operações relacionadas a templates de exercícios

- **DTOs (Data Transfer Objects)**: Objetos para transferência de dados entre camadas
  - `workout_dto.py` - DTO para treinos
  - `routine_dto.py` - DTO para rotinas
  - `exercise_template_dto.py` - DTO para templates de exercícios

#### 3. Camada de Infraestrutura (`hevyai/infrastructure/`)

Implementa os detalhes técnicos e integrações externas.

- **Repositórios (Implementações)**: Implementações concretas dos repositórios do domínio
  - `hevy_workout_repository.py` - Implementa WorkoutRepository
  - `hevy_routine_repository.py` - Implementa RoutineRepository
  - `hevy_exercise_template_repository.py` - Implementa ExerciseTemplateRepository

- **Cliente da API**: Interage com a API do Hevy
  - `hevy_client.py` - Cliente para a API do Hevy

- **Persistência**: Configuração do banco de dados e ORM
  - `models.py` - Modelos do Django para persistência

#### 4. Camada de Apresentação (`hevyai/presentation/`)

Lida com a interação com o usuário e apresentação dos dados.

- **API REST**: Endpoints da API Django REST Framework
  - `views.py` - Viewsets e views do DRF
  - `serializers.py` - Serializers do DRF
  - `urls.py` - Configuração de URLs

- **Frontend React**: Interface de usuário
  - Componentes React
  - Páginas e views
  - Gerenciamento de estado (Redux ou Context API)

## Padrões de Design e Decisões Arquiteturais

### Padrões Adotados

1. **Repository Pattern**: Abstrai o acesso a dados, permitindo trocar a fonte de dados sem impactar o domínio.
2. **DTO Pattern**: Transfere dados entre camadas sem expor detalhes de implementação.
3. **Dependency Injection**: Reduz acoplamento entre componentes.
4. **Factory Pattern**: Para criação de objetos complexos.

### Convenções de Código

- **Nomenclatura**: 
  - Classes em PascalCase
  - Métodos e variáveis em snake_case
  - Constantes em UPPER_SNAKE_CASE

- **Documentação**: 
  - Docstrings para classes e métodos
  - Comentários para lógica complexa
  - Tipo de anotações para parâmetros e retornos

## Fluxo de Desenvolvimento

### Implementação do Backend

1. Configurar estrutura básica do projeto Django
2. Implementar a camada de domínio
3. Implementar a camada de infraestrutura com o cliente da API Hevy
4. Implementar a camada de aplicação com casos de uso
5. Implementar a API REST com Django REST Framework

### Implementação do Frontend

1. Configurar projeto React com TailwindCSS
2. Implementar componentes UI básicos
3. Implementar páginas para listagem e visualização de treinos
4. Implementar páginas para listagem e visualização de rotinas
5. Implementar visualização de templates de exercícios

## Considerações de Segurança

- Armazenamento seguro da chave de API do Hevy usando variáveis de ambiente
- Implementação de autenticação e autorização
- Validação de dados de entrada
- Proteção contra CSRF e XSS

## Plano de Testes

- **Testes Unitários**: Para domínio e aplicação
- **Testes de Integração**: Para infraestrutura e API
- **Testes End-to-End**: Para fluxos completos de usuário

## Estratégia de Implantação

1. Configuração de CI/CD com GitHub Actions
2. Implantação em contêineres Docker
3. Configuração de ambiente de produção

## Roadmap de Funcionalidades

### Versão 1.0
- Visualização de treinos
- Visualização de rotinas
- Visualização de templates de exercícios

### Versão 2.0
- Análise de métricas de treino
- Gráficos de progresso
- Recomendações de treino

### Versão 3.0
- Integração com outros serviços de fitness
- Recursos sociais e compartilhamento