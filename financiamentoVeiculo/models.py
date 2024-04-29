from django.db import models

# Create your models here.

class FinanciamentoVeiculo(models.Model):
    id = models.AutoField(primary_key=True)
    valor_veiculo = models.DecimalField(max_digits=10, decimal_places=2)
    entrada = models.DecimalField(max_digits=10, decimal_places=2)   
    prazo_meses = models.IntegerField()
