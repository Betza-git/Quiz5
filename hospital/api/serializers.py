"""Serializers:
Realizar validaciones de los datos usando raise"""

from .models import Pacientes, Doctor, Especialidad, Cita, DoctoresEspecialidades
from rest_framework import serializers

class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'
     

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate(self, data):
            # Validar que el nombre no esté vacío
            if not data.get('nombre'):
                raise serializers.ValidationError("El nombre del doctor es obligatorio.")
            # Validar que los años de experiencia sean un número positivo
            if data.get('anos_experiencia') < 0:
                raise serializers.ValidationError("Los años de experiencia deben ser un número positivo.")
            return data
        
class EspecialidadSerializer(serializers.ModelSerializer):
    doctores = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Especialidad
        fields = '__all__'


    

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'

    def validate(self, data):
        doctor = data.get('doctor')
        paciente = data.get('paciente')
        # impedir que un paciente tenga una cita con el mismo doctor el mismo día
        if Cita.objects.filter(doctor=doctor, paciente=paciente, fecha=data.get('fecha')).exists():
            raise serializers.ValidationError("El paciente ya tiene una cita con este doctor ese día.")

        return data


class DoctoresEspecialidadesSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    especialidad = serializers.PrimaryKeyRelatedField(queryset=Especialidad.objects.all())
    class Meta:
        model = DoctoresEspecialidades
        fields = ['doctor', 'especialidad']
 





