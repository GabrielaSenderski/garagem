from django.db import models

class Cor(models.Model):
    nome = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Cores'