from django.db import models
from apps.filiais.models import Filial
from apps.departamentos.models import Departamento


class Funcionario(models.Model):
    fun_nome = models.CharField(max_length=150)
    fun_fil_id = models.ForeignKey(Filial, on_delete=models.PROTECT)
    fun_email = models.CharField(max_length=150)
    fun_dep_id = models.ManyToManyField(Departamento)
    fun_celular = models.CharField(max_length=15)
    fun_resp_dep = models.BooleanField(default=False)

    def __str__(self):
        return self.fun_nome
