from django.db import models


class Grau(models.Model):
    grau_nome = models.CharField(max_length=30)
    grau_descricao = models.CharField(max_length=60)
    grau_urgencia = models.IntegerField()

    def __str__(self):
        return self.grau_nome
