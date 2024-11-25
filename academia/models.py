from django.db import models

class Formacao(models.Model): 
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)

    def __str__(self):
        return self.nome
    
class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    cidade  = models.CharField(max_length=100)

    
    def __str__(self):
        return self.nome

class Meta:
    verbose_name_plural = 'Instituicoes'

class Instrutor(models.Model):
    nome = models.CharField(max_length=100)
    email  = models.EmailField(max_length=100)
    datanascimento  = models.DateField(blank=True, null=True)