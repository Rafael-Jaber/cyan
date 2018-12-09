from django.db import models


class Documento(models.Model):
    doc_nome = models.CharField(max_length=50)
    doc_arquivo = models.FileField()

    def __str__(self):
        return self.doc_nome
