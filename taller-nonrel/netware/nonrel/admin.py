from django.contrib import admin
from .models import Accion


class AccionAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'tipo', 'url')

admin.site.register(Accion, AccionAdmin)
