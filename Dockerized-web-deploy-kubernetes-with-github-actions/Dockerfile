# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia todo el contenido de la aplicación al contenedor
COPY . /app/

# Instala Flask y Flask-Cors
RUN pip install --no-cache-dir flask flask-cors

# Expon el puerto 5000 donde la app estará escuchando
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
