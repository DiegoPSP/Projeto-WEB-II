from django.contrib import admin
from .models import Tarefa, Inscricao, Projeto, Categoria, Comentario

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criador', 'data_criacao')
    search_fields = ('nome', 'descricao')
    list_filter = ('criador',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nome',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'autor', 'data_criacao')
    list_filter = ('autor', 'data_criacao')
    search_fields = ('texto', 'tarefa__titulo', 'autor__username')
    autocomplete_fields = ('tarefa', 'autor')


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'projeto', 'categoria', 'criador', 'data_limite', 'status')
    list_filter = ('status', 'projeto', 'categoria', 'data_limite', 'criador')
    search_fields = ('titulo', 'descricao')
    list_editable = ('status', 'categoria') 
    date_hierarchy = 'data_limite'
    autocomplete_fields = ('criador', 'projeto', 'categoria') 

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('tarefa', 'colaborador', 'data_inscricao')
    list_filter = ('tarefa', 'colaborador')
    search_fields = ('tarefa__titulo', 'colaborador__username')
    autocomplete_fields = ('tarefa', 'colaborador')