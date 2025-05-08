from django.urls import path 
from .views import (
    PacientesListCreateView, PacienteDetailView,
    DoctorListCreateView, DoctorDetailView,
    EspecialidadListCreateView, EspecialidadDetailView,
    CitaListCreateView, CitaDetailView,
    DoctoresEspecialidadesListCreateView, DoctoresEspecialidadesDetailView
)


urlpatterns = [
   
    path('pacientes/', PacientesListCreateView.as_view(), name='pacientes-list-create'),
    path('pacientes/<int:pk>/', PacienteDetailView.as_view(), name='paciente-detail'),
    path('doctores/', DoctorListCreateView.as_view(), name='doctores-list-create'),
    path('doctores/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('especialidades/', EspecialidadListCreateView.as_view(), name='especialidades-list-create'),
    path('especialidades/<int:pk>/', EspecialidadDetailView.as_view(), name='especialidad-detail'),
    path('citas/', CitaListCreateView.as_view(), name='citas-list-create'),
    path('citas/<int:pk>/', CitaDetailView.as_view(), name='cita-detail'),
    path('doctores-especialidades/', DoctoresEspecialidadesListCreateView.as_view(), name='doctores-especialidades-list-create'),
    path('doctores-especialidades/<int:pk>/', DoctoresEspecialidadesDetailView.as_view(), name='doctores-especialidades-detail'),
]