# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0002_auto_20140910_1355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
    ]
