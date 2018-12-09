from django.db import models


class Status(models.Model):
    std_nome = models.CharField(max_length=50)
    std_descricao = models.CharField(max_length=100)
    std_conslusivo = models.BooleanField(default=False)

    def __str__(self):
        return self.std_nome
