# Use uma imagem base com Python
FROM python:3.11

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos da aplicação
COPY . .

# Exponha a porta que sua aplicação Flask usa
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
