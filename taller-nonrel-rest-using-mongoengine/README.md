# API/REST con Bases de datos No Relacionales (nonrel). Taller de django-rest-framework-mongoengine.

Este archivo contiene un proyecto de ejemplo con el que explicamos el uso de mongoengine y django-rest-framework-mongoengine.

Para hacer uso de el es necesario primero tener una base de datos mongo. La instalamos [comandos para ubuntu]
```
#    apt-get install  mongodb mongodb-server mongodb-clients
```

A continuación crear un entorno de virtualenv

```
$    virtualenv taller-nonrel-rest-using-mongoengine
```

A continuación entrar en la carpeta taller- y activar el entorno

```
$    cd taller-nonrel-rest-using-mongoengine
$    source bin/activate
```

Y posteriormente instalar Django 1.6.5 y el resto de las librerias que requiere el proyecto:
```
$    pip install django==1.6.5                 # mongoadmin no funciona el Django 1.7 
$    pip install djangorestframework
$    pip install mongoengine
$    pip install django-rest-framework-mongoengine
$    pip install mongodbforms 

$    git clone https://github.com/jschrewe/django-mongoadmin.git
$    cd django-mongoadmin/
$    python setup.py install
```

Lo siguiente es copiar el proyecto dentro de la carpeta taller-nonrel-rest-using-mongoengine

Entramos dentro del proyecto, sincronizamos la BD (creamos el usuario admin) y arrancamos el servidor

```
$    python manage.py syncdb
$    python manage.py runserver
```
