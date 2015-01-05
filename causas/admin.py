from django.contrib import admin
from .models import *
# Register your models here.

class DocumentoInline(admin.StackedInline):
    model = Documento
    extra = 1


#duda con la carta de cobro
class DemandaAdmin(admin.ModelAdmin):
	# fieldsets = (
	# 	(None,{
	# 		'fields':('asegurado', 'ingreso', 'tribunal', 'rol', 'monto', 'tipo'),
	# 		}),
	# 	('Siniestro', {
	# 		'fields':('numero_de_siniestro', 'fecha_siniestro', 'fecha_demanda', 'comuna', 'lugar', 
	# 			'patente_vehiculo','chofer', 'alcolemia'),
	# 		}),
		
	# 	('Notificacion', {
	# 		'fields':('notificacion', 'carta_de_cobro', 'pagada',  'factura' )
	# 		}),
	# 	('Comparendo', {
	# 		'fields':('fecha_comparendo',),
	# 		}),
	# 	('Estado', {
	# 		'fields':('estado',)
	# 		})


	# )
    fieldsets = (
        (None, {
            'fields': ('numero_de_siniestro', 'ingreso', 'comuna', 'tribunal', 
            'rol', 'fecha_siniestro',  'notificacion','fecha_comparendo',  'tipo',
            'conductor', 'patente',  
            'alcolemia',  'estado'), 
        }),
        ('Recupero', {
            'fields':('fecha_demanda','monto',('factura', 'pagada'), 'carta_de_cobro'),
            'classes':('collapse',),

        }),
        ('Asegurado', {
            'fields': ('rut_asegurado', 'nombre_asegurado', 'direccion_asegurado', 
            'telefono_asegurado', 'correo_asegurado'),
            #'classes':('collapse',),
        
        }),
        ('Tercero', {
            'fields':('rut_tercero', 'nombre_tercero', 'telefono_tercero', 'correo_tercero', 'gestion_de_cobro'),
            #'classes':('collapse',),
        }),
    )

    list_display = ('numero_de_siniestro', 'rol', 'comuna', 'fecha_comparendo', 'nombre_asegurado')
    inlines = [
		DocumentoInline,
	]





admin.site.register(Tribunal)
admin.site.register(Demanda, DemandaAdmin)
