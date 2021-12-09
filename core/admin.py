from django.contrib import admin
from .models import Cargo, Servico, Colaborador, Recursos


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')


@admin.register(Recursos)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'icone', 'ativo', 'modificado')
