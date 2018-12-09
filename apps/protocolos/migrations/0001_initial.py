# Generated by Django 2.1.4 on 2018-12-09 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('interacoes', '0001_initial'),
        ('documentos', '0001_initial'),
        ('funcionarios', '0002_auto_20181209_1829'),
        ('grau', '0001_initial'),
        ('status', '0001_initial'),
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Protocolo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prot_descricao', models.TextField()),
                ('prot_dep_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamentos.Departamento')),
                ('prot_documentos_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='documentos.Documento')),
                ('prot_fun_origin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario')),
                ('prot_grau', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='grau.Grau')),
                ('prot_interacoes_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='interacoes.Interacoes')),
                ('prot_status_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='status.Status')),
            ],
        ),
    ]