from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self) -> str:
        return self.nome
    
class Curso(models.Model):
    NIVEL = (
        ('B', 'Basico'),
        ('I', 'Intermediario'),
        ('A', 'avançado'),
    )
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1 ,choices=NIVEL, blank=False, null=False, default='B')#Não pode ficar vazio

    def __str__(self) -> str:
        return self.descricao
    
