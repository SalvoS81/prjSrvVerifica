from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from modelVerifica import views
from modelVerifica.views import Operazione_di_verificaViewSet, UserViewSet, api_root
from rest_framework import renderers

operazione_di_verifica_list = Operazione_di_verificaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
operazione_di_verifica_detail = Operazione_di_verificaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('operazione_di_verifica/', 
        operazione_di_verifica_list,
        name='operazione_di_verifica-list'),
    path('operazione_di_verifica/<int:pk>/',
       operazione_di_verifica_detail,
        name='operazione_di_verifica-detail'),
    path('users/', 
        user_list,
        name='user-list'),
    path('users/<int:pk>/',
        user_detail,
        name='user-detail'),    
])
