from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from .models import PhoneNumber, Phonebook
from .serializers import PhoneNumberSerializer, PhonebookSerializer


class PhoneNumberAPIView(generics.ListCreateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer


class PhoneNumberAPIViewPut(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhoneNumberSerializer

    def retrieve(self, request, *args, **kwargs):
        qs = PhoneNumber.objects.filter(pk=kwargs.get('pk')).first()
        serializer = self.get_serializer(qs)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        qs = PhoneNumber.objects.filter(pk=kwargs.get('pk')).first()
        serializer = self.get_serializer(qs, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        qs = PhoneNumber.objects.filter(pk=kwargs.get('pk')).first()
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhonebookAPIView(generics.ListCreateAPIView):
    queryset = Phonebook.objects.all()
    serializer_class = PhonebookSerializer


class PhonebookAPIViewPut(generics.RetrieveUpdateDestroyAPIView):
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
