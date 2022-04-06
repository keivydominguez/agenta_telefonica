from django.contrib import admin
from django.urls import path
from rest_framework import routers
from apps.agenda.api import PhoneNumberAPIView, PhoneNumberAPIViewPut, PhonebookAPIView, PhonebookAPIViewPut

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', PhonebookAPIView.as_view(), name='agenda_api'),
    path('agenda/<int:pk>/', PhonebookAPIViewPut.as_view(), name='agenda_put'),
    path('agenda/telefono/', PhoneNumberAPIView.as_view(), name='telefono_api'),
    path('agenda/telefono/<int:pk>/',
         PhoneNumberAPIViewPut.as_view(), name='telefono_put'),
]
