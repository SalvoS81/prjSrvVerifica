#from django.shortcuts import render

from django.contrib.auth.models import User
#from rest_framework import mixins
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
from modelVerifica.models import Operazione_di_verifica
from modelVerifica.permissions import IsOwnerOrReadOnly
from modelVerifica.serializers import (Operazione_di_verifica_Serializer,
                                       UserSerializer)


""" @api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'operazione_di_verifica': reverse('operazione_di_verifica-list', request=request, format=format)
    })
 """

class Operazione_di_verificaViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
   
    """
    queryset = Operazione_di_verifica.objects.all()
    serializer_class = Operazione_di_verifica_Serializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    #@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    #def highlight(self, request, *args, **kwargs):
    #    snippet = self.get_object()
    #    return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

"""
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
"""

"""
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
"""

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
