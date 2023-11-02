# backend

Esta API-REST es un ejercicio para una evaluación.

## Requerimientos

- Python >= 3.7
- Pipenv
- PostgreSQL >= 10

## Entorno de desarrollo

1. Crea una base de datos para el proyecto:

   ```bash
   CREATE USER evaluacion WITH PASSWORD 'evaluacion';
   CREATE DATABASE evaluacion OWNER evaluacion;
   ```

2. En la carpeta raíz, crea un archivo `.env` con el siguiente contenido:

   ```
       DEBUG=True
       SECRET_KEY=somesupersecretkey
       ALLOWED_HOSTS=*
       DB_USER=evaluacion
       DB_PASSWORD=evaluacion
       DB_NAME=evaluacion
       DB_HOST=127.0.0.1
       DB_PORT=5432
       FRONTEND_URL=frontenturl

   ```

3. Instala las dependencias del proyecto:

   ```bash
   pipenv install
   ```

4. Ejecuta las migraciones y crea un superusuario:

   ```bash
   pipenv run python manage.py migrate
   pipenv run python manage.py createsuperuser
   ```

5. Ejecuta el servidor de desarrollo:

   ```bash
   pipenv run python manage.py runserver
   ```
