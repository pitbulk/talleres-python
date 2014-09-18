# API-REST. Taller de django-rest-framework

Este archivo contiene un proyecto de ejemplo con el que explicamos el uso de django-rest-framework

Para hacer uso de el es necesario crear un entorno de virtualenv

```
$   virtualenv taller-rest
```

A continuación entrar en la carpeta taller-rest y activar el entorno

```
$   cd taller-rest
$   source bin/activate
```

Y posteriormente instalar las librerias que requiere el proyecto
```
$    pip install django djangorestframework
```

Lo siguiente es copiar el proyecto dentro de la carpeta taller-rest

Entramos dentro del proyecto, sincronizamos la BD (creamos el usuario admin) y arrancamos el servidor

```
$    python manage.py syncdb
$    python manage.py runserver
```
