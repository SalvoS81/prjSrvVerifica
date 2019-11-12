#from django.shortcuts import render

#from rest_framework import mixins
from rest_framework import generics, permissions
from django.contrib.auth.models import User

# Create your views here.
from modelVerifica.models import Operazione_di_verifica
from modelVerifica.serializers import Operazione_di_verifica_Serializer, UserSerializer
from modelVerifica.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'operazione_di_verifica': reverse('operazione_di_verifica-list', request=request, format=format)
    })

class Operazione_di_verifica_List(generics.ListCreateAPIView):
    queryset = Operazione_di_verifica.objects.all()
    serializer_class = Operazione_di_verifica_Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class Operazione_di_verifica_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Operazione_di_verifica.objects.all()
    serializer_class = Operazione_di_verifica_Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

""" 
class Operazioni_di_verifica_List(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Operazione_di_verifica.objects.all()
    serializer_class = Operazione_di_verifica_Serializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Operazione_di_verifica_Detail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Operazione_di_verifica.objects.all()
    serializer_class = Operazione_di_verifica_Serializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 
"""
