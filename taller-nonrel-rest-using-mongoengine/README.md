# Bases de datos No Relacionales (nonrel). Taller de django-mongodb-engine.

Este archivo contiene un proyecto de ejemplo con el que explicamos el uso de mongodb y django-mongodb-engine

Para hacer uso de el es necesario primero tener una base de datos mongo. La instalamos [comandos para ubuntu]
```
#    apt-get install  mongodb mongodb-server mongodb-clients
```

A continuación crear un entorno de virtualenv

```
$    virtualenv taller-nonrel:x
```

A continuación entrar en la carpeta taller-nonrel y activar el entorno

```
$    cd taller-nonrel
$    source bin/activate
```

Y posteriormente instalar un fork de Django (django-nonrel) y el resto de librerias que requiere el proyecto
```
$   pip install git+https://github.com/django-nonrel/django@nonrel-1.5
$   pip install git+https://github.com/django-nonrel/djangotoolbox
$   pip install git+https://github.com/django-nonrel/mongodb-engine
```

Lo siguiente es copiar el proyecto dentro de la carpeta taller-nonrel

Entramos dentro del proyecto, sincronizamos la BD (creamos el usuario admin) y arrancamos el servidor

```
$    python manage.py syncdb
$    python manage.py runserver
```
