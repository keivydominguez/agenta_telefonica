from django.contrib import admin
from .models import PhoneNumber, Phonebook

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['phone', 'etiqueta']
    list_filter = ['phone', 'etiqueta']

class PhonebookAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'nickname', 'phone', 'email', 'relationship']
    list_filter = ['name', 'nickname', 'phone', 'relationship']

admin.site.register(PhoneNumber)
admin.site.register(Phonebook)