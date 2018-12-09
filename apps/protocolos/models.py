from django.db import models
from apps.funcionarios.models import Funcionario
from apps.status.models import Status
from apps.grau.models import Grau
from apps.interacoes.models import Interacoes
from apps.documentos.models import Documento
from apps.departamentos.models import Departamento


class Protocolo(models.Model):
    prot_fun_origin = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    prot_grau = models.ForeignKey(Grau, on_delete=models.PROTECT)
    prot_descricao = models.TextField()
    prot_dep_id = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    prot_documentos_id = models.ForeignKey(Documento, on_delete=models.PROTECT)
    prot_interacoes_id = models.ForeignKey(Interacoes, on_delete=models.PROTECT)
    prot_status_id = models.ForeignKey(Status, on_delete=models.PROTECT)

    def __str__(self):
        return self.prot_dep_id.dep_nome
