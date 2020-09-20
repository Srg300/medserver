from django.db import models
from django.contrib.auth.models import User

class Pill(models.Model):
    """лекарство"""
    title =  models.CharField(verbose_name='Название лекарства', max_length=100)

    def __str__(self):
        return self.title



class Appointment(models.Model):
    """назначение"""
    title = models.CharField(verbose_name='назначение', blank=True, max_length=250)
    dose = models.FloatField(verbose_name='Дозировка в мг.', null= True)
    desciprion = models.CharField(verbose_name='Описание', blank=True, max_length=250)
    
    def __str__(self):
        return self.title


class Specialization(models.Model):
    title = models.CharField(verbose_name='сепциализация', blank=True, max_length=250)


class Recepi(models.Model):
    '''
    Рецепт 
    '''
    pill = models.ForeignKey(Pill, related_name='pill', on_delete=models.DO_NOTHING)
    title = models.CharField(verbose_name='назначение', blank=True, max_length=250)
    dose = models.FloatField(verbose_name='Дозировка в мг.', null= True)
    desciprion = models.CharField(verbose_name='Описание', blank=True, max_length=250)
    owner = models.ForeignKey('Patient', verbose_name='пациент', on_delete=models.DO_NOTHING, related_name='recepi', null=True)


    def __str__(self):
        return str(self.title) 


class Doctor(models.Model):
    '''
    Модель для доктора
    '''    
    STATUS_CHOICES = [
        ('Терапевт','терапевт'),
        ('Хирург','хирург'),
        ('Кардиолог','Кардиолог')
    ]
    user = models.OneToOneField(User, verbose_name='Пользователь',
    on_delete=models.DO_NOTHING, related_name='doc_profile', null=True)
    first_name = models.CharField(verbose_name='Имя', max_length=100)
    last_name = models.CharField(verbose_name='Фамилия', max_length=100)
    phone = models.CharField(verbose_name='Телефон',max_length=20 )
    specialization = models.CharField(verbose_name= 'Специализация', choices=STATUS_CHOICES, default='Терапевт', max_length=100)
    # specialization = models.ForeignKey(Specialization, verbose_name='Специализация', on_delete=models.DO_NOTHING, related_name='spec', null=True)

    

    def __str__(self):
        return self.first_name +' '+ self.last_name



class Patient(models.Model):
    '''
    Моедль пациента
    '''
    user = models.OneToOneField(User, verbose_name='Пользователь',
     on_delete=models.CASCADE,related_name='patient_profile', null=True)
    doctor = models.ForeignKey(Doctor, verbose_name='Доктор',
     on_delete=models.DO_NOTHING,related_name='doctor', null=True,)
    first_name = models.CharField(verbose_name='Имя', max_length=100)
    last_name = models.CharField(verbose_name='Фамилия', max_length=100)
    diagnosis = models.CharField(verbose_name='Диагноз', max_length=250,blank=True)
    phone = models.CharField(verbose_name='Телефон', blank=True, max_length=20)
    address = models.CharField(verbose_name='Адрес', blank=True, max_length=100)
    # recepi = models.ForeignKey(Recepi, on_delete=models.CASCADE, verbose_name='Список лекарств',related_name='patient', blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' +  self.last_name


