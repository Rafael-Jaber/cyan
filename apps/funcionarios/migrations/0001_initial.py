# Generated by Django 2.1.4 on 2018-12-09 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamentos', '0001_initial'),
        ('filiais', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fun_nome', models.CharField(max_length=150)),
                ('fun_email', models.CharField(max_length=150)),
                ('fun_celular', models.CharField(max_length=15)),
                ('fun_dep_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departamentos.Departamento')),
                ('fun_fil_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='filiais.Filial')),
            ],
        ),
    ]
