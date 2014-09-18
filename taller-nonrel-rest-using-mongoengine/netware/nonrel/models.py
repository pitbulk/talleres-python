from mongoengine.django.auth import User
from mongoengine import Document, ReferenceField, StringField
from django.utils.translation import ugettext_lazy as _


class Accion(Document):
    user = ReferenceField(User)
    tipo = StringField(max_length=100)
    url = StringField()

    def get_username(self):
        user = User.objects.get(id=self.user.id)
        return user.username

    class Meta:
        verbose_name = _(u'Accion')
        verbose_name_plural = _(u'Acciones')

        def __unicode__(self):
            return '%s | %s %s' % (self.get_username(), self.tipo, self.url)

    class Admin:
        pass
