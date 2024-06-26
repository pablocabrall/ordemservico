from django.db import models

class Cliente(models.Model):
    razao_social = models.CharField('Razão Social', max_length=120, unique=True)
    cnpj = models.CharField('CNPJ', max_length=14, null=True, blank=True)

    class Meta:
        ordering = ('razao_social',)
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
    
    def __str__(self):
        return f'{self.razao_social}'
