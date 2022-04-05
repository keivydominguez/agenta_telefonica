from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PhoneNumber, Phonebook
from .serializers import PhoneNumberSerializer, PhonebookSerializer

class PhoneNumberAPIView(APIView):
    def get (self, request):
        phonenumber = PhoneNumber.objects.all()
        phonenumber_serializer = PhoneNumberSerializer(phonenumber, many=True)
        return Response(phonenumber_serializer.data)

class PhonebookAPIView(APIView):
    def get (self, request):
        phonebook = Phonebook.objects.all()
        phonebook_serializer = PhonebookSerializer(phonebook, many=True)
        return Response(phonebook_serializer.data)