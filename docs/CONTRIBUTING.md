# Guia de Contribuição

Obrigado pelo seu interesse em contribuir com o projeto HevyAI! Este documento fornece diretrizes para contribuir com o projeto.

## Fluxo de Trabalho do Git

1. Faça um fork do repositório
2. Clone o seu fork para sua máquina local
3. Crie uma branch para sua feature ou correção de bug:
   ```bash
   git checkout -b feature/nome-da-feature
   ```
   ou
   ```bash
   git checkout -b fix/nome-do-bug
   ```
4. Implemente suas alterações seguindo as convenções do projeto
5. Adicione e faça commit das suas alterações:
   ```bash
   git add .
   git commit -m "Descrição clara e concisa da alteração"
   ```
6. Envie as alterações para o seu fork:
   ```bash
   git push origin feature/nome-da-feature
   ```
7. Abra um Pull Request para a branch principal do repositório original

## Padrões de Código

### Backend (Python/Django)

- Siga o PEP 8 para estilo de código Python
- Use docstrings para documentar classes e funções
- Adicione tipagem estática com type hints
- Escreva testes unitários para novas funcionalidades
- Siga os princípios SOLID e a arquitetura DDD

### Frontend (React/TypeScript)

- Use o ESLint e Prettier para formatação consistente
- Siga as convenções de nomenclatura do React (PascalCase para componentes)
- Organize componentes em arquivos separados
- Utilize TypeScript para tipagem estática
- Implemente testes para componentes

## Processo de Pull Request

1. Verifique se todos os testes estão passando antes de enviar o PR
2. Forneça uma descrição clara do que a alteração faz
3. Relacione o PR a uma issue existente, se aplicável
4. Espere a revisão de pelo menos um mantenedor do projeto

## Reportando Bugs

Se você encontrar um bug, por favor abra uma issue com:

- Uma descrição clara do bug
- Passos para reproduzir
- Comportamento esperado vs. comportamento observado
- Capturas de tela, se aplicável
- Informações sobre seu ambiente (navegador, sistema operacional, etc.)

## Sugerindo Melhorias

Para sugerir melhorias:

1. Abra uma issue com o rótulo "enhancement"
2. Descreva claramente a melhoria e os benefícios que ela trará
3. Discuta a implementação proposta, se aplicável

## Dúvidas?

Se você tiver dúvidas sobre como contribuir, abra uma issue com o rótulo "question" ou entre em contato com os mantenedores do projeto.

Agradecemos sua contribuição para tornar o HevyAI melhor!