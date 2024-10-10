from django.db import models
'''O sistema deve permitir que Pedro
 registre
informações sobre cada treino
 ou competição,
 incluindo data, distância percorrida,
tempo, localização, e condições climáticas.'''
# Create your models here.

class Pedro(models.Model):
    tipo = models.CharField(
      choices=(
          ("treino", "Treino"),
            ("competicao", "Competição"),
        ),
        max_length=12, default = "")
    data = models.DateField(null=True, blank=True)
    distancia_percorrida_km = models.IntegerField(null=True, blank=True)
    tempo = models.TimeField(null=True, blank=True)
    localizacao = models.CharField(max_length = 100, null=True, blank=True)
    condicoes_climaticas = models.CharField(null=True, blank=True, max_length = 50)
    def __str__(self):
        return self.localizacao