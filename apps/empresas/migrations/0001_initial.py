# Generated by Django 2.1.4 on 2018-12-09 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_raiz_cnpj', models.CharField(max_length=15)),
                ('emp_nome', models.CharField(max_length=80)),
            ],
        ),
    ]