from django.shortcuts import get_object_or_404
from .models import Libro, Autor
from .serializers import LibroSerializer, AutorSerializer
from rest_framework import viewsets
from rest_framework.response import Response

 
class LibroViewSet(viewsets.ModelViewSet):
 
    serializer_class = LibroSerializer
    queryset = Libro.objects.all()
 
    def retrieve(self, request, pk=None):
        queryset = Libro.objects.all()
        libro = get_object_or_404(queryset, pk=pk)
        serializer = LibroSerializer(libro)
        return Response(serializer.data)


class AutorViewSet(viewsets.ModelViewSet):
 
    serializer_class = AutorSerializer
    queryset = Autor.objects.all()
