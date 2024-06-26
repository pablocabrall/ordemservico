from django.db import models

class Servico(models.Model):
    titulo = models.CharField('Titulo', max_length=100)

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'serviço'
        verbose_name_plural = 'serviços'
    
    def __str__(self):
        return f'{self.titulo}'

