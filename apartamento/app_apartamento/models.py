from django.db import models
# Create your models here.
class Apartamento(models.Model):
    numero = models.IntegerField()
    qtdQuartos = models.IntegerField()
    proprietario = models.CharField(max_length=50)
    valor_Condominio = models.DecimalField(decimal_places=2, max_digits=2)

    def __str__(self):
        self.proprietario
