from rest_framework import viewsets, generics
from .models import Aluno, Curso, Matricula
from .serializers import (
    AlunoSerializer, CursoSerializer, 
    MatriculaSerializer, ListaMatriculasAlunosSerializer
)

class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibe todos os alunos e alunas """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """ Exibe todos os cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """ Exibe todas a matriculas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    """ Listando as matriculas de Um aluno """
    def 