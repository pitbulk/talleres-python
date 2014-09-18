from django.contrib import admin
from .models import Autor, Libro


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    pass

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    pass