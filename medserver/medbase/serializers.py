from django.contrib.auth.models import User
from rest_framework import serializers, fields
from rest_framework.relations import PrimaryKeyRelatedField

from .models import *
from djoser.serializers import UserCreateSerializer, UserSerializer

from drf_writable_nested.serializers import WritableNestedModelSerializer

from django.forms.models import model_to_dict


class CurentUserSerializer(serializers.ModelSerializer):
    """ Сериализатор, для текущего пользователя """
    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff', 'is_superuser']


class UserSerializer(serializers.ModelSerializer):
    """
    для отображения пользователя
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class CreateSuperuserSerializer(serializers.ModelSerializer):
    """
    для отображения пользователя
    """
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password','email', 'is_staff', 'is_superuser']

    def create(self, validated_data):        
        user = User.objects.create_user(**validated_data)
        user.is_staff = True
        user.is_superuser = True
        user.save(update_fields=['is_staff', 'is_superuser'])
        return user

class PillSerializer(serializers.ModelSerializer):
    """
    таблетка
    """
    class Meta:
        model = Pill
        fields = ['id', 'title']


class RecepiListSerializer(serializers.ModelSerializer):
    pill = serializers.ReadOnlyField(source='pill.title')
    class Meta:
        model = Recepi
        fields = ['id','pill', 'title', 'dose', 'desciprion','owner']



class RecepiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recepi
        fields = ['id','pill', 'title', 'dose', 'desciprion','owner']
        depth = 1


class RecepiUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recepi
        fields = ['id','pill', 'title', 'dose', 'desciprion']


class RecepiCreateSerializier(serializers.ModelSerializer):
    """
    Создание рецептов
    """
    class Meta:
        model = Recepi
        fields = ['pill', 'title', 'dose', 'desciprion', 'owner']


class RecepiSerializerForPatient(serializers.ModelSerializer):
    """
    Для представления данных пациенту
    """ 
    class Meta:
        model = Recepi
        fields = ['id','pill', 'title', 'dose', 'desciprion']
        depth = 1


class DoctorCreateSerializer(serializers.ModelSerializer):
    """ создание пациента """
    user = UserCreateSerializer()
    class Meta:
        model = Doctor
        fields = ['user','first_name', 'last_name', 'phone', 'specialization']
    
    def create(self, validated_data):        
        user_data = validated_data.pop('user')
        # Для того, что бы правильно создался User, сгенерировался hash пароль, 
        # лучше использовать  User.objects.create_user()
        user = User.objects.create_user(**user_data)
        user.is_staff = True
        user.save(update_fields=["is_staff"])
        doctor = Doctor.objects.create(user=user, **validated_data)
        return doctor


class DoctorListSerializier(serializers.ModelSerializer):
    """
    Список докторов
    """
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Doctor
        fields = ['id','user','first_name', 'last_name', 'phone', 'specialization']


class DoctorDetailSerializier(serializers.ModelSerializer):
    """
    Детализация доктора
    """
    specialization = Doctor.STATUS_CHOICES
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Doctor
        fields = ['id', 'user', 'user_id', 'first_name', 'last_name', 'phone', 'specialization']


class DoctorDetailSerializierForPatient(serializers.ModelSerializer):
    """
    Детализация доктора
    """
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = Doctor
        fields = ['id','user_id','first_name', 'last_name', 'phone', 'specialization']

class PatientListSerializier(serializers.ModelSerializer):
    """
    Список пациентов
    """
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Patient
        fields = ['id', 'user', 'first_name', 'last_name', 'diagnosis', 'doctor']
        depth=1

class PatientDetailSerializier(serializers.ModelSerializer):
    """
    Детализация пациента
    """
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    recepi = RecepiSerializerForPatient(many=True)
    doctor = DoctorDetailSerializierForPatient()
    class Meta:
        model = Patient
        fields = ['user_id', 'id', 'user', 'first_name', 'last_name', 'diagnosis', 'phone', 'address', 'recepi', 'doctor']
        
class PatientUpdateSerializier(serializers.ModelSerializer):
    """
    Обновление пациента
    """
    class Meta:
        model = Patient
        fields = ['id', 'user', 'first_name', 'last_name', 'diagnosis', 'phone', 'address',  'doctor']


class PatientCreateSerializer(serializers.ModelSerializer):
    """ создание пациента """
    user = UserCreateSerializer()
    doctor = PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'phone', 'address','doctor', 'user']
    
    def create(self, validated_data):        
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        user.set_password
        patient = Patient.objects.create(user=user, **validated_data)
        return patient

