from rest_framework import serializers
from .models import PhoneNumber, Phonebook


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'


class PhonebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonebook
        fields = '__all__'
