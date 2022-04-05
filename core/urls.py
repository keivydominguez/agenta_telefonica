from django.contrib import admin
from django.urls import path
from apps.agenda.api import PhoneNumberAPIView, PhonebookAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', PhonebookAPIView.as_view(), name = 'agenda_api')
]
