from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 
from .models import Pacientes, Doctor, Especialidad, Cita, DoctoresEspecialidades
from .serializers import PacientesSerializer, DoctorSerializer, EspecialidadSerializer, CitaSerializer, DoctoresEspecialidadesSerializer
"""Vistas:
Implementar vistas para cada modelo usando las clases genéricas
ListCreateAPIView y RetrieveUpdateDestroyAPIView."""


class PacientesListCreateView(ListCreateAPIView):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer

# Recuperar, actualizar y eliminar
class PacienteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer

class DoctorListCreateView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class EspecialidadListCreateView(ListCreateAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class EspecialidadDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class CitaListCreateView(ListCreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class CitaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class DoctoresEspecialidadesListCreateView(ListCreateAPIView):
    queryset = DoctoresEspecialidades.objects.all()
    serializer_class = DoctoresEspecialidadesSerializer

class DoctoresEspecialidadesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = DoctoresEspecialidades.objects.all()
    serializer_class = DoctoresEspecialidadesSerializer

