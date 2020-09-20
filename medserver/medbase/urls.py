from django.urls import path, include
from .views import *
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('pills', PillsViewList)
router.register('recepis', RecepiViewList)
router.register('doctors', DoctorViewList)
router.register('patients', PatientViewList)


urlpatterns = [
    path('', include(router.urls)),

    # path('pills/', PillsViewList.as_view()),
    path('pill/<int:pk>', PillDetailView.as_view()),
    path('pill/create/', PillCreateView.as_view()),

    # path('recepis/', RecepiViewList.as_view()),
    path('recepi/<int:pk>', RecepiViewDetail.as_view()),
    path('recepi/update/<int:pk>', RecepiUpdateDetail.as_view()),
    path('recepi/create/', RecepiCreateView.as_view()),

    # path('doctors/', DoctorViewList.as_view()),
    path('doctor/create/', DoctorCreateView.as_view()),
    path('doctor/<int:pk>', DoctorViewDetail.as_view()),

    path('patient/create/', PatientCreateView.as_view()),
    path('patients_/', views.get_patient_list),    
    path('patient/<int:pk>', PatientDetailView.as_view()),    
    path('patient/update/<int:pk>', PatientUpdateView.as_view()),    

    path('superuser/create/', SuperUser.as_view()),
    path('', include('djoser.urls')),
    # path('', include('djoser.urls.authtoken')),
]