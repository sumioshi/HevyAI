FROM python:3.10-slim

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.5.1

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"

# Configurar diretório de trabalho
WORKDIR /app

# Copiar arquivos de configuração
COPY pyproject.toml poetry.lock* ./

# Configurar poetry para não criar ambiente virtual
RUN poetry config virtualenvs.create false

# Instalar dependências
RUN poetry install --no-dev --no-interaction

# Copiar o projeto
COPY . .

# Expor a porta
EXPOSE 8000