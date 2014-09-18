from mongoengine.django.auth import User
from mongoadmin import site, DocumentAdmin
from .models import Accion


class AccionAdmin(DocumentAdmin):
    list_display = ('get_username', 'tipo', 'url')


class UserAdmin(DocumentAdmin):
    pass

site.register(User, UserAdmin)
site.register(Accion, AccionAdmin)
