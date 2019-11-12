from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from modelVerifica import views

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('operazione_di_verifica/', 
        views.Operazione_di_verifica_List.as_view(),
        name='operazione_di_verifica-list'),
    path('operazione_di_verifica/<int:pk>/',
        views.Operazione_di_verifica_Detail.as_view(),
        name='operazione_di_verifica-detail'),
    path('users/', 
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail'),    
])
