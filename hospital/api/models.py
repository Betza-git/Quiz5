from django.db import models

"""Crear cinco modelos (tablas):
o Pacientes: Información básica de los pacientes (nombre, edad, etc.)
o Doctores: Datos de los doctores (nombre, años de experiencia, etc.)
o Especialidades: Listado de especialidades médicas (Cardiología,
Pediatría, etc.)
o Citas: Representa una cita médica entre un paciente y un doctor. Debe
tener campos como fecha, hora y motivo.
o DoctoresEspecialidades: Tabla intermedia personalizada que relacione
doctores con sus especialidades. 

2. Relaciones esperadas:
 Un doctor puede tener múltiples especialidades y una especialidad puede
tener varios doctores (ManyToMany con tabla intermedia).
 Una cita debe relacionar a un doctor y a un paciente (ForeignKey en
ambos casos).
"""

class Pacientes(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre}, {self.edad}, {self.direccion}, {self.telefono}"

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    anos_experiencia = models.IntegerField()
    especialidad = models.ForeignKey('Especialidad', on_delete=models.CASCADE, related_name='doctores')
    especialidades = models.ManyToManyField('Especialidad', through='DoctoresEspecialidades') 
    
    def __str__(self):
        return f"{self.nombre}, {self.anos_experiencia}, {self.especialidad}"

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    def __str__(self):
        return f"{self.nombre}, {self.descripcion}"
   

class Cita(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"Cita: {self.fecha} {self.hora} - {self.paciente} con {self.doctor}"

class DoctoresEspecialidades(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('doctor', 'especialidad')
    def __str__(self):
        return f"{self.doctor} - {self.especialidad}"

  

          
