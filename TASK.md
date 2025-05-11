# Tarefas do Projeto HevyAI

Este arquivo contém as tarefas e o status de desenvolvimento do projeto HevyAI.

## Tarefas Principais

### Configuração e Infraestrutura
- [x] Configurar estrutura inicial do projeto
- [x] Configurar Docker e Docker Compose
- [x] Configurar Poetry para gerenciamento de dependências
- [ ] Configurar ambiente de testes
- [ ] Configurar CI/CD (futuro)

### Backend - Django/DRF
- [x] Configurar arquivo settings.py
- [x] Implementar arquitetura DDD
- [x] Criar entidades de domínio
- [x] Criar interfaces de repositórios
- [x] Implementar cliente de API Hevy
- [x] Implementar repositórios para API Hevy
- [x] Criar DTOs para transferência de dados
- [x] Implementar casos de uso
- [x] Criar serializers para a API REST
- [x] Criar viewsets para a API REST
- [ ] Implementar autenticação de usuários
- [ ] Implementar caching local de dados
- [ ] Configurar testes unitários

### Frontend - React/TailwindCSS
- [x] Configurar estrutura básica do React
- [x] Configurar TailwindCSS
- [ ] Implementar componentes base
- [ ] Implementar layout principal
- [ ] Implementar página de dashboard
- [ ] Implementar listagem de treinos
- [ ] Implementar detalhes de treinos
- [ ] Implementar listagem de rotinas
- [ ] Implementar detalhes de rotinas
- [ ] Implementar listagem de modelos de exercícios
- [ ] Implementar sistema de autenticação
- [ ] Configurar testes de componentes

### Documentação
- [x] Criar README.md com instruções de configuração
- [x] Criar PLANNING.md com detalhes da arquitetura
- [x] Criar TASK.md para monitoramento de tarefas
- [ ] Documentar API REST
- [ ] Criar documentação de uso do sistema

### Implantação
- [ ] Preparar ambiente de produção
- [ ] Configurar servidor web (Gunicorn/Nginx)
- [ ] Implementar backup de dados
- [ ] Implantar em servidor de produção

## Tarefas em Andamento

- Implementação do cliente da API Hevy
- Configuração do ambiente de desenvolvimento

## Tarefas Concluídas

- Configuração da estrutura do projeto (10/05/2025)
- Criação da arquitetura DDD para Django (10/05/2025)
- Implementação das entidades de domínio (10/05/2025)
- Implementação dos repositórios básicos (10/05/2025)

## Descobertas Durante o Trabalho

- A API do Hevy requer uma chave de API no header 'api-key'
- A API do Hevy utiliza nomenclatura diferente da nossa arquitetura (ex: 'title' em vez de 'name')
- Possíveis limitações da API para operações de escrita (criação/atualização/exclusão)