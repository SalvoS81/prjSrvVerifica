from django.contrib.auth.models import User
from rest_framework import serializers

from modelVerifica.models import Operazione_di_verifica

"""
class UserSerializer(serializers.ModelSerializer):
    Operazione_di_verifica = serializers.PrimaryKeyRelatedField(many=True, queryset=Operazione_di_verifica.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'Operazione_di_verifica']


class Operazione_di_verifica_Serializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Operazione_di_verifica
        fields = ['id', 'matricola_verificatore', 'data_registrazione', 'risposte', 'vettura', 'linea', 'foglio', 'owner',]
"""

class Operazione_di_verifica_Serializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
   
    class Meta:
        model = Operazione_di_verifica
        fields = ['url', 'id', 'matricola_verificatore', 'data_registrazione', 'risposte', 'vettura', 'linea', 'foglio', 'owner',]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    Operazione_di_verifica = serializers.HyperlinkedRelatedField(many=True, view_name='operazione_di_verifica-detail', read_only=True)

    class Meta:
       model = User
       fields = ['url', 'id', 'username', 'Operazione_di_verifica']