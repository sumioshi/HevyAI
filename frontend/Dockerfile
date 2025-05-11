FROM node:18-alpine

WORKDIR /app

# Instalar create-react-app globalmente
RUN npm install -g create-react-app

# Copiar arquivos de configuração
COPY package.json ./

# Instalar dependências específicas
RUN npm install --legacy-peer-deps
RUN npm install ajv@6.12.6 ajv-keywords@3.5.2 --legacy-peer-deps

# Copiar código fonte
COPY . .

# Expor a porta
EXPOSE 3000

# Comando para iniciar
CMD ["npm", "start"]