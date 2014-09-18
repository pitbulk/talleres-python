from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from mongoengine.django.auth import User
from nonrel.models import Accion
from apirest.serializers import AccionSerializer, UserSerializer

#from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_mongoengine import viewsets


class AccionViewSet(viewsets.ModelViewSet):
    model = Accion
    queryset = Accion.objects.all()
    serializer_class = AccionSerializer

    def retrieve(self, request, pk=None):
        queryset = Accion.objects.all()
        accion = get_object_or_404(queryset, pk=pk)
        serializer = AccionSerializer(accion)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        queryset = Accion.objects.all()
        accion = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(accion)
        return Response(serializer.data)

#class AccionList(ListCreateAPIView):
#    queryset = Accion.objects.all()
#    serializer_class = AccionSerializer

#class AccionDetail(RetrieveUpdateDestroyAPIView):
#    queryset = Accion.objects.all()
#    serializer_class = AccionSerializer