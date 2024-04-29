from django.db import models

# Create your models here.

class SimulacaoEmprestimo(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    valor_emprestimo = models.DecimalField(max_digits=10, decimal_places=2)
    taxa_juros = models.DecimalField(max_digits=5, decimal_places=2)
    prazo_meses = models.IntegerField()