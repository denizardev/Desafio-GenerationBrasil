# Use a imagem base do Python
FROM python:3.12

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de dependências
COPY requirements.txt requirements.txt

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação
COPY . .

# Exponha a porta que a aplicação usa
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
