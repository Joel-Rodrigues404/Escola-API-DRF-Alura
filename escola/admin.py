from django.contrib import admin
from .models import (
    Aluno, Curso, Matricula
)
# Register your models here.


class AlunosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ('nome',)

admin.site.register(Aluno, AlunosAdmin)

class CursosAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    list_per_page = 20
    search_fields = ('codigo_curso',)

admin.site.register(Curso, CursosAdmin)

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id', )

admin.site.register(Matricula, MatriculaAdmin)