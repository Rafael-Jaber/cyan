from django.db import models


class Interacoes(models.Model):
    int_mensagem = models.TextField()
    int_data = models.DateField()
    int_data_visualizado = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.int_mensagem