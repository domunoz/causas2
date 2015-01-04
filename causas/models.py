#coding:utf-8
from django.db import models

# Create your models here.
class Persona(models.Model):
	RUT = models.CharField(max_length=144)
	nombre = models.CharField(max_length=144)
	apellido_paterno = models.CharField(max_length=144)
	apellido_materno = models.CharField(max_length=144)

class Procurador(Persona):
	pass

class Asegurado(Persona):
	pass

class Chofer(Persona):
	pass	

class Comuna(models.Model):
	nombre = models.CharField(max_length=140)



class Vehiculo(models.Model):
	patente = models.CharField(max_length=144)
	dueno = models.ForeignKey('Asegurado')

class Tribunal(models.Model):
	nombre = models.CharField(max_length=144)
	comuna = models.CharField(max_length=144)


class Demanda(models.Model):
	TIPO_CHOICES = (
		('R', 'Recupero'),
		('D', 'Defensa'),
		('C', 'Confuso'),
		)
	#data
	numero_de_siniestro = models.IntegerField('SNTRO.')
	asegurado = models.ForeignKey('Asegurado', null=True, blank=True)
	ingreso = models.DateField(null=True, blank=True)
	lugar = models.CharField(max_length=144, null=True, blank=True)
	# comuna = models.CharField(max_length=144)
	tribunal = models.ForeignKey('Tribunal', null=True, blank=True)
	rol = models.CharField(max_length=144, unique=True)
	monto = models.FloatField(null=True, blank=True)
	tipo = models.CharField('Tipo', max_length=1, choices=TIPO_CHOICES, null=True, blank=True)
	fecha_siniestro = models.DateField('ACC.', null=True, blank=True)#acc
	fecha_demanda = models.DateField('Demanda', null=True, blank=True)
	notificacion = models.DateField('Notificación', null=True, blank=True)
	pagada = models.BooleanField('PAGADA', default=False)#la notificacion que se paga al actuario
	alcolemia = models.FloatField('Alcoholemia', null=True, blank=True)
	factura = models.BooleanField('FACTURA', default=True)
	carta_de_cobro = models.DateField(null=True, blank=True)
	fecha_comparendo = models.DateField('Comparendo', null=True, blank=True)
	estado = models.TextField(null=True, blank=True)
		
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

