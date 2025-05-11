# Arquitetura e Planejamento do HevyAI

## Visão Geral da Arquitetura

O HevyAI utiliza uma arquitetura baseada em Domain-Driven Design (DDD) adaptada para o ecossistema Django. Essa abordagem nos permite organizar o código de forma que reflita o domínio do problema, facilitando a manutenção e evolução do sistema.

## Camadas da Arquitetura

### 1. Camada de Domínio (Domain Layer)

Esta é a camada central da aplicação, onde residem as entidades de negócio, objetos de valor, interfaces de repositórios e serviços de domínio.

**Estrutura:**
- `/domain/entities/`: Contém as entidades principais (Workout, Routine, ExerciseTemplate)
- `/domain/value_objects/`: Objetos de valor imutáveis 
- `/domain/repositories/`: Interfaces para acesso a dados
- `/domain/services/`: Lógica de negócio complexa que envolve múltiplas entidades

### 2. Camada de Aplicação (Application Layer)

Orquestra o fluxo entre o domínio e a infraestrutura. Contém os casos de uso da aplicação e DTOs (Data Transfer Objects).

**Estrutura:**
- `/application/use_cases/`: Implementações dos casos de uso
- `/application/dtos/`: Objetos para transferência de dados entre camadas

### 3. Camada de Infraestrutura (Infrastructure Layer)

Implementa as interfaces definidas na camada de domínio e fornece detalhes técnicos.

**Estrutura:**
- `/infrastructure/repositories/`: Implementações concretas dos repositórios
- `/infrastructure/api/`: Clientes para APIs externas (Hevy API)

### 4. Camada de Apresentação (Presentation Layer)

Responsável pela interface com o usuário, incluindo API REST e interface web.

**Estrutura:**
- `/presentation/rest/`: API REST com Django Rest Framework
- `/presentation/rest/viewsets/`: ViewSets para expor a API
- `/presentation/rest/serializers/`: Serializers para conversão de dados

### 5. Frontend (React + TailwindCSS)

Interface web moderna e responsiva construída com React e estilizada com TailwindCSS.

**Estrutura:**
- `/frontend/src/components/`: Componentes React reutilizáveis
- `/frontend/src/pages/`: Páginas da aplicação
- `/frontend/src/hooks/`: Custom hooks para lógica compartilhada
- `/frontend/src/services/`: Serviços para comunicação com o backend

## Padrões de Design

1. **Repository Pattern**: Abstrai o acesso a dados através de interfaces.
2. **Use Case Pattern**: Encapsula a lógica de negócio específica em casos de uso.
3. **DTO Pattern**: Transfere dados entre camadas sem expor detalhes de implementação.
4. **Factory Pattern**: Facilita a criação de objetos complexos.

## Fluxo de Dados

1. O usuário interage com a interface React
2. A interface faz requisições à API REST
3. A API REST encaminha as requisições para os ViewSets apropriados
4. Os ViewSets utilizam os casos de uso da camada de aplicação
5. Os casos de uso orquestram a lógica utilizando as entidades de domínio
6. Os repositórios implementados na camada de infraestrutura comunicam-se com a API externa do Hevy
7. Os dados são retornados seguindo o caminho inverso

## Padrões de Codificação

### Naming Conventions

- **Arquivos Python**: snake_case (exemplo: workout_repository.py)
- **Classes**: PascalCase (exemplo: WorkoutRepository)
- **Métodos e Variáveis**: snake_case (exemplo: get_by_id)
- **Constantes**: UPPER_SNAKE_CASE (exemplo: DEFAULT_PAGE_SIZE)
- **Arquivos TypeScript/React**: PascalCase para componentes (exemplo: WorkoutList.tsx)

### Documentação

- Todas as classes e métodos públicos devem ter docstrings em português.
- Comentários específicos para lógicas complexas utilizando o formato: `# Razão: <explicação>`.
- Manter o README.md e TASK.md atualizados.

## Estrutura de Bancos de Dados

O projeto utiliza PostgreSQL para persistência de dados, principalmente para caching local de dados da API Hevy e autenticação de usuários.

## Gestão de Dependências

- Backend: Poetry para gerenciamento de dependências Python
- Frontend: NPM para gerenciamento de dependências JavaScript/TypeScript

## Ambiente de Desenvolvimento

O ambiente de desenvolvimento é containerizado com Docker e Docker Compose, permitindo fácil configuração e garantindo consistência entre ambientes.

## Testes

- Testes unitários utilizando pytest para o backend
- Testes de componentes utilizando React Testing Library para o frontend
- Os testes seguem a estrutura espelhada do código fonte em /tests/

## CI/CD

Futuramente, será implementado um pipeline de CI/CD para automatizar testes e deployment.

## Segurança

- Chaves de API armazenadas em variáveis de ambiente
- Autenticação JWT para a API interna
- HTTPS para todas as comunicações em produção