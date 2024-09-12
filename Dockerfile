# Use a imagem oficial do Python
FROM python:3.12-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copie o restante dos arquivos do projeto
COPY . .

# Defina a variável de ambiente para o Flask
ENV FLASK_APP=app.py

# Comando para rodar a aplicação Flask
CMD ["flask", "run", "--host=0.0.0.0"]
