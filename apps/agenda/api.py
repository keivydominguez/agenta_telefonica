from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import PhoneNumber, Phonebook
from .serializers import PhoneNumberSerializer, PhonebookSerializer


class PhoneNumberAPIView(generics.ListCreateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer


class PhoneNumberAPIViewPut(generics.CreateAPIView):
    serializer_class = PhoneNumberSerializer

    def get(self, request, pk=None):
        qs = PhoneNumber.objects.filter(id=pk).first()
        serializer = self.get_serializer(qs)
        return Response(serializer.data)

    def put(self, request, pk=None):
        qs = PhoneNumber.objects.filter(id=pk).first()
        serializer = self.get_serializer(qs, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        qs = PhoneNumber.objects.filter(id=pk).first()
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhonebookAPIView(generics.ListCreateAPIView):
    queryset = Phonebook.objects.all()
    serializer_class = PhonebookSerializer


class PhonebookAPIViewPut(generics.CreateAPIView):
    serializer_class = PhonebookSerializer

    def get(self, request, pk=None):
        qs = Phonebook.objects.filter(id=pk).first()
        serializer = self.get_serializer(qs)
        return Response(serializer.data)

    def put(self, request, pk=None):
        qs = Phonebook.objects.filter(id=pk).first()
        serializer = self.get_serializer(qs, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        qs = Phonebook.objects.filter(id=pk).first()
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
