from django.contrib.auth.models import User
from django.shortcuts import render

from .serializers import *
from .models import *
from .permissions import *

from rest_framework.decorators import api_view, permission_classes, renderer_classes, parser_classes
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view
from rest_framework.views import Response
from rest_framework.views import APIView


class PillsViewList(viewsets.ModelViewSet):
    """список всех таблеток"""
    serializer_class = PillSerializer
    queryset = Pill.objects.all()


class PillDetailView(generics.RetrieveUpdateDestroyAPIView):
    """данные и редактирование таблетки"""
    serializer_class = PillSerializer
    queryset = Pill.objects.all()


class PillCreateView(generics.CreateAPIView):
    """данные и редактирование таблетки"""
    serializer_class = PillSerializer
    queryset = Pill.objects.all()
    permission_classes = [IsSuperUser]


class RecepiViewList(viewsets.ModelViewSet):
    """Список рецептов"""    
    serializer_class = RecepiListSerializer
    queryset = Recepi.objects.all()
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_superuser:
            recepi = Recepi.objects.all()
            return recepi
        else:
            user = self.request.user
            patient = Patient.objects.get(user=user)
            recepi = Recepi.objects.filter(owner=patient)
            return recepi



class RecepiViewDetail(generics.RetrieveAPIView):
    """Детали рецепта"""    
    serializer_class = RecepiSerializer
    queryset = Recepi.objects.all()
    permission_classes = [ForRecepi]


class RecepiUpdateDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Обновление рецепта """
    serializer_class = RecepiUpdateSerializer
    queryset = Recepi.objects.all()
    permission_classes = [ForRecepi]


class RecepiCreateView(generics.CreateAPIView):
    """ создание рецепта """
    serializer_class = RecepiCreateSerializier
    queryset = Recepi.objects.all()
    permission_classes = [IsAdminUser|IsSuperUser]


class DoctorViewList(viewsets.ModelViewSet):
    """ Список докторов """
    serializer_class = DoctorListSerializier
    queryset = Doctor.objects.all()
    permission_classes = [IsStaffUser]

    def get_queryset(self):
        if self.request.user.is_superuser:
            doctor = Doctor.objects.all()
            return doctor
        else:
            user = self.request.user
            doctor = Doctor.objects.filter(user=user)
            return doctor

class DoctorViewDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Детализация доктора """
    serializer_class = DoctorDetailSerializier
    # queryset = Doctor.objects.all()
    permission_classes = [IsStaffUser]

    def get_queryset(self):
        if self.request.user.is_superuser:
            doctor = Doctor.objects.all()
            return doctor
        else:
            user = self.request.user
            doctor = Doctor.objects.filter(user=user)
            return doctor


class DoctorCreateView(generics.CreateAPIView):
    """ Создание доктора """
    serializer_class = DoctorCreateSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsSuperUser]


# /api/patients/ 
class PatientViewList(viewsets.ModelViewSet):
    """ Детализация всех пациентов """
    serializer_class = PatientListSerializier
    queryset = Patient.objects.all()
    permission_classes = [IsDoctor]

    def get_queryset(self):
        if self.request.user.is_superuser:
            patients = Patient.objects.all()
            return patients
        else:
            user = self.request.user
            doctor = Doctor.objects.get(user=user)
            patients = Patient.objects.filter(doctor=doctor)
            return patients


# /api/patients_/
@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_patient_list(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            patients = Patient.objects.all()
            serializers_patient = PatientListSerializier(patients, many=True)
            return Response({'results': serializers_patient.data},status=status.HTTP_200_OK)
        else:
            user = request.user
            doctor = Doctor.objects.get(user=user)
            patients = Patient.objects.filter(doctor=doctor)
            serializers_patient = PatientListSerializier(patients, many=True)
            return Response({'results': serializers_patient.data},status=status.HTTP_200_OK)
    return Response(serializers_patient.errors, status=status.HTTP_400_BAD_REQUEST)  


# /api/patient/{id}
class PatientDetailView(generics.RetrieveAPIView):
    """ Детализация пациента """   
    serializer_class = PatientDetailSerializier
    permission_classes = [IsSuperUser|IsDoctor]

    def get_queryset(self):
        if self.request.user.is_superuser:
            patients = Patient.objects.all()
            return patients
        else:
            user = self.request.user
            doctor = Doctor.objects.get(user=user)
            patients = Patient.objects.filter(doctor=doctor)
            return patients


# /api/patient/update/{id}
class PatientUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """ Обновление пациента """
    serializer_class = PatientUpdateSerializier
    queryset = Patient.objects.all()
    permission_classes = [IsSuperUser|IsDoctor]

    def get_queryset(self):
        if self.request.user.is_superuser:
            patients = Patient.objects.all()
            return patients
        else:
            user = self.request.user
            doctor = Doctor.objects.get(user=user)
            patients = Patient.objects.filter(doctor=doctor)
            return patients


# /api/patient/create/
class PatientCreateView(generics.CreateAPIView):
    """ Детализация создания пациента """    
    serializer_class = PatientCreateSerializer
    permission_classes = [IsSuperUser|IsDoctor]

    def get_queryset(self):
        if self.request.user.is_superuser:
            patients = Patient.objects.all()
            return patients
        else:
            user = self.request.user
            doctor = Doctor.objects.get(user=user)
            patients = Patient.objects.filter(doctor=doctor)
            return patients


    def post(self, request, *args, **kwargs):
        user = self.request.user
        # doctor = Doctor.objects.get(user=user)
        patients = Patient.objects.all()
        return self.create(request, *args, **kwargs)


class SuperUser(generics.CreateAPIView):
    """ создание супер юзера """
    serializer_class = CreateSuperuserSerializer
    permission_classes = [IsSuperUser]

