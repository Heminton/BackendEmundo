from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.catalogos.departamento.models import Departamento

"""
Clientes
"""

class Cliente(models.Model):
    
    GENERO_CHOICES = [('M', 'Masculino'), ('F', 'Femenino')]
    
    nombre = models.CharField(verbose_name='Nombre', max_length=100)
    apellido = models.CharField(verbose_name='Apellido', max_length=100)
    edad = models.IntegerField(verbose_name='Edad',validators=[MinValueValidator(1), MaxValueValidator(100)])
    departamento = models.ForeignKey(Departamento, verbose_name='Departamento', on_delete=models.PROTECT)
    genero = models.CharField(verbose_name='Género', max_length=1, choices=GENERO_CHOICES)
    class Meta:
        verbose_name_plural = 'Clientes'
        
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"



