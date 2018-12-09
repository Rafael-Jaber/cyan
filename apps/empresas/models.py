from django.db import models


class Empresa(models.Model):
    emp_raiz_cnpj = models.CharField(max_length=15)
    emp_nome = models.CharField(max_length=80)

    def __str__(self):
        return self.emp_nome
