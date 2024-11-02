# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias a la imagen
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install pytest-selenium==2.0.1

# Copia el código fuente de pruebas en el contenedor
COPY . .

# Comando por defecto para ejecutar los tests
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-v"]
