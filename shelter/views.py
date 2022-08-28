from rest_framework import generics
from .serializer import AnimalSerializer
from .models import Animal


class AnimalList(generics.ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalDetail(generics.RetrieveAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
