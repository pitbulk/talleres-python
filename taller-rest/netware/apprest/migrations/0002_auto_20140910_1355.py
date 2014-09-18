# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelOptions(
            name='libro',
            options={'verbose_name': 'Libros', 'verbose_name_plural': 'Libro'},
        ),
    ]
