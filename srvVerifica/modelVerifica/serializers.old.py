from rest_framework import serializers

from modelVerifica.models import Operazione_di_verifica


class Operazione_di_verifica_Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    matricola_verificatore = serializers.CharField(required=True, max_length=5)
    data_registrazione = serializers.DateTimeField(read_only=True)
    #questionario = serializers.PrimaryKeyRelatedField()
    risposte = serializers.CharField(style={'base_template': 'textarea.html'})
    vettura = serializers.IntegerField()
    linea = serializers.CharField(max_length=20)
    foglio = serializers.IntegerField()

    def create(self, validated_data):
        return Operazione_di_verifica.objects.create(**validated_data)
        #return super().create(validated_data)

    def update(self, instance, validated_data):
        #instance.matricola_verificatore = validated_data.get('matricola_verificatore', instance.matricola_verificatore)
        instance.risposte = validated_data.get('risposte', instance.risposte)
        vettura = validated_data.get('vettura', instance.vettura)
        linea = validated_data.get('liena', instance.linea)
        foglio = validated_data.get('foglio', instance.foglio)
        instance.save()
        return instance

        #return super().update(instance, validated_data)
