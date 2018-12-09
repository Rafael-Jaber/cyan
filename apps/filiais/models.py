from django.db import models
from apps.empresas.models import Empresa


class Filial(models.Model):
    fil_emp_id = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    fil_cnpj = models.CharField(max_length=15)
    fil_cidade = models.CharField(max_length=80)

    def __str__(self):
        return self.fil_cnpj
