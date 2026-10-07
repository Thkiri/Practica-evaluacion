from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    activa = models.BooleanField(default=True, verbose_name="Activa")

    
class OrdenReparacion(models.Model):
    ESTADO_CHOICES = (
        ('INGRESADO', 'Ingresado'),
        ('EN_PROCESO', 'En Proceso'),
        ('LISTO', 'Listo'),
        ('ENTREGADO', 'Entregado'),
    )

    codigo_orden = models.CharField(max_length=10, unique=True, verbose_name="Código de Orden")
    patente_vehiculo = models.CharField(max_length=8, verbose_name="Patente")
    modelo_vehiculo = models.CharField(max_length=100, verbose_name="Modelo del Vehículo")
    cliente_nombre = models.CharField(max_length=150, verbose_name="Nombre del Cliente")
    costo_estimado = models.IntegerField(verbose_name="Costo Estimado")
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='INGRESADO',
        verbose_name="Estado"
    )
    fecha_ingreso = models.DateField(auto_now_add=True, verbose_name="Fecha de Ingreso")
    especialidad = models.ForeignKey(
        Especialidad,
        on_delete=models.CASCADE,
        related_name='ordenes',
        verbose_name="Especialidad"
    )
