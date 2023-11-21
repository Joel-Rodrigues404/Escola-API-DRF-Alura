from rest_framework import viewsets
from .models import Aluno, Curso
from .serializers import AlunoSerializer, CursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibe todos os alunos e alunas """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    """ Exibe todos os cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
