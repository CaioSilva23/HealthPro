from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=70, blank=False, null=False)
    celular = models.CharField(max_length=14, blank=False, null=False)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome


class AvaliacaoDiaria(models.Model):
    RATING_CHOICES = (
        ('E', 'Excelente'),
        ('B', 'Bom'),
        ('R', 'Ruim'),
        ('P', 'Péssimo'),
    )
    
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)

    anotacao_positiva = models.TextField(null=True, blank=True)
    anotacao_negativa = models.TextField(null=True, blank=True)


class AlertasCrise(models.Model):
    RATING_CHOICES = (
        ('P', 'Pânico'),
        ('A', 'Ansiedade'),
        ('D', 'Depressão'),
    )
    nota_alerta = models.CharField(max_length=1, choices=RATING_CHOICES)

    horario_acontecimento = models.DateTimeField()
    horario_superou_crise = models.DateTimeField()
