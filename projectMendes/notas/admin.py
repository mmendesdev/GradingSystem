from django.contrib import admin

from .models import Categoria, Nota


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "usuario", "categoria", "criado_em")
    search_fields = ("titulo", "conteudo")
    list_filter = ("categoria", "criado_em")
    date_hierarchy = "criado_em"


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

    search_fields = ("nome",)
