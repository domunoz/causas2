#coding:utf-8
from django.db import models
from cl_reg_prov_com import COMUNA_CHOICES

# Create your models here.
class Persona(models.Model):
    def __unicode__(self):
        return self.nombre 


class Procurador(Persona):
    pass
class Chofer(Persona):
    pass	

class Comuna(models.Model):
    nombre = models.CharField(max_length=140)

    def __str__(self):
        return self.nombre 

class Tribunal(models.Model):
    nombre = models.CharField(max_length=144)
    comuna = models.CharField(max_length=144)


class Demanda(models.Model):
    TIPO_CHOICES = (
		('R', 'Recupero'),
		('D', 'Defensa'),
		('C', 'Confuso'),
		)

    TRIBUNALES = (
            ('PL', 'Policía Local'),
            ('FI', 'Fiscalía'),
            ('JC', 'Juzgado Civil'),
            ('OT', 'Otros'),

            
    )
	#data
    numero_de_siniestro = models.IntegerField('SNTRO.', unique=True) #debe cambiar al field correspondiente
#    asegurado = models.ForeignKey('Asegurado', null=True, blank=True)
    ingreso = models.DateField(null=True, blank=True)
#    lugar = models.CharField(max_length=144, null=True, blank=True)
    comuna = models.CharField(max_length=5, choices=COMUNA_CHOICES, null=True, blank=True)
	# comuna = models.CharField(max_length=144)
#    tribunal = models.ForeignKey('Tribunal', null=True, blank=True)
    tribunal = models.CharField(choices=TRIBUNALES, max_length=2, null=True, blank=True)


    rol = models.CharField('ROL/RUC', max_length=144, unique=True, help_text="número de causa que entrega fiscalía")
#    comuna = models.ForeignKey(Comuna)
    tipo = models.CharField('Tipo', max_length=1, choices=TIPO_CHOICES, null=True, blank=True)
    fecha_siniestro = models.DateField('ACC.', null=True, blank=True)#acc
    conductor = models.CharField(max_length=140, null=True, blank=True)
    patente = models.CharField(max_length=10, null=True, blank=True)
    
    fecha_demanda = models.DateField('Demanda', null=True, blank=True)
    notificacion = models.DateField('Notificación', null=True, blank=True)
    alcolemia = models.FloatField('Alcoholemia', null=True, blank=True)
    fecha_comparendo = models.DateField('Comparendo', null=True, blank=True)
    estado = models.TextField(null=True, blank=True)

    #recupero 
    
    factura = models.BooleanField('FACTURA', default=True)
    pagada = models.BooleanField('PAGADA', default=False)#la notificacion que se paga al actuario
    carta_de_cobro = models.DateField(null=True, blank=True)
    monto = models.FloatField(null=True, blank=True)

    #tercero = models.CharField(max_length=140)
		
    #asegurado
    rut_asegurado= models.CharField('RUT', max_length=144, null=True, blank=True)
    nombre_asegurado  = models.CharField('nombre', max_length=144, null=True, blank=True)
    telefono_asegurado  = models.CharField('teléfono', max_length=140, null=True, blank=True)
    direccion_asegurado = models.CharField('dirección', max_length=140, null=True, blank=True) 
    correo_asegurado = models.EmailField('correo', max_length=140, null=True, blank=True)




    class Meta:
        verbose_name = 'Causa'

	
	#Notificacion
	#Asegurado
	#Informacion del siniestro
	# patente_vehiculo = models.CharField(max_length=144)
	# chofer = models.CharField(max_length=144)
	#comparendo
	#estado

# class Siniestro(models.Model):
# 	demanda = models.ForeignKey('Demanda')

# class Comparendo(models.Model):
# 	fecha = models.DateField()
# 	demanda = models.ForeignKey('Demanda')


class Documento(models.Model):
    archivo = models.FileField(upload_to='/documentos')
    demanda = models.ForeignKey('Demanda')

