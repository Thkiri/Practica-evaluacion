from django.contrib import admin
from .models import Especialidad, OrdenReparacion



class OrdenReparacionInline(admin.TabularInline):
    model = OrdenReparacion
    extra = 1

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activa', 'total_ordenes']
    inlines = [OrdenReparacionInline]

    @admin.display(description='Total Órdenes')
    def total_ordenes(self, obj):
        return obj.ordenes.count()

@admin.register(OrdenReparacion)
class OrdenReparacionAdmin(admin.ModelAdmin):
    list_display = [
        'codigo_orden',
        'patente_vehiculo',
        'modelo_vehiculo',
        'cliente_nombre',
        'costo_estimado',
        'estado',
        'fecha_ingreso',
        'especialidad'
    ]
    list_filter = ['estado', 'especialidad', 'fecha_ingreso']
    list_editable = ['estado']
    search_fields = [
        'codigo_orden',
        'patente_vehiculo',
        'cliente_nombre',
        'especialidad__nombre'
    ]
    actions = ['marcar_como_listo']

    @admin.action(description='Marcar seleccionadas como LISTO')
    def marcar_como_listo(self, request, queryset):
        actualizados = queryset.update(estado='LISTO')
        self.message_user(request, f"{actualizados} órdenes fueron actualizadas a LISTO exitosamente.")
