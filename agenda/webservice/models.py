from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)
    idade = models.SmallIntegerField()
    telefone = models.CharField(max_length=80)
    
    class Meta:
        ordering = ["apelido"]