from django.db import models
from django.utils.translation import ugettext_lazy as _


class Autor(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)

    class Meta:
        verbose_name = _(u'Autor')
        verbose_name_plural = _(u'Autores')

        def __unicode__(self):
            return '%s %s' % (self.nombre, self.apellido)

    class Admin:
        pass


class Libro(models.Model):
    nombre = models.TextField(max_length=100)
    editorial = models.TextField(max_length=100)
    genero = models.TextField(max_length=100)
    autor = models.ForeignKey(Autor)

    class Meta:
        verbose_name = _(u'Libro')
        verbose_name_plural = _(u'Libros')

        def __unicode__(self):
            return '%s - %s' % (self.nombre, self.editorial)

    class Admin:
        pass
