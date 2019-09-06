# djangotest


Para correr el proyecto

version de python necesaria: 3.6

1) pip install pipenv

2) pipenv install (Estando dentro del proyecto) / pipenv sync

3) pipenv shell (activar el entorno virtual)

4) crear una base de datos en postgres

5) Crear djangoTest/secret.py y añadir configuracion

6) python manage.py makemigrations

7) python manage.py migrate

8) python manage.py runserver

PARA CREAR SUPER USUARIO

1) python manage.py createsuperuser

PARA TENER DATOS DE MUESTRA

1) Crear 2 libros orden guia biblica y proyecto vuelve a casa (Se puede desde el admin)

2) python manage.py loaddata chapters.json

3) python manage.py loaddata subchapters.json

4) python manage.py loaddata content.json

ESTRUCTURA

Accounts: Cuenta con la información de los usuarios

app: Contenido del proyecto (modelos)

djangoTest: directorio base - vistas del proyecto

api: REST API del proyecto (Documentarte con django rest framework)

static: Archivos estaticos

templates: plantillas del proyecto

utils: herramientas del proyecto

PARA CORRER EL SCRIPT 

python script.py

