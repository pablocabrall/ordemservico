# Generated by Django 5.0.6 on 2024-06-27 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
            ],
            options={
                'verbose_name': 'serviço',
                'verbose_name_plural': 'serviços',
                'ordering': ('titulo',),
            },
        ),
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao', models.CharField(choices=[('pe', 'Pendente'), ('ca', 'Cancelado'), ('an', 'Andamento'), ('ap', 'Aprovado')], max_length=2, verbose_name='Situação')),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ordem_servicos', to='cliente.cliente', verbose_name='cliente')),
            ],
            options={
                'verbose_name': 'ordem de serviço',
                'verbose_name_plural': 'ordens de serviço',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='OrdemServicoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='valor')),
                ('proxima_visita', models.DateField(blank=True, null=True, verbose_name='Próxima Visita')),
                ('ordem_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordem_servico_itens', to='servico.ordemservico', verbose_name='ordem de serviço')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordem_servico_item_servicos', to='servico.servico', verbose_name='serviço')),
            ],
            options={
                'verbose_name': 'item da ordem de serviço',
                'verbose_name_plural': 'itens da ordens de serviço',
                'ordering': ('-pk',),
            },
        ),
    ]
