# Escolha a imagem base do Python 3.8
FROM python:3.8

# Defina o diretório de trabalho como /app
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências especificadas em requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie o diretório atual para o contêiner em /app
COPY . .

# Especifique o comando que será executado quando o contêiner for iniciado
CMD ["python", "app.py"]
