from django.db import models

# Create your models here.
class Operazione_di_verifica(models.Model):
    matricola_verificatore = models.CharField("Matricola del verificatore", max_length=5, editable=False)
    data_registrazione = models.DateTimeField("Data di registrazione", auto_now_add=True)
    #questionario = models.ForeignKey('Questionario', on_delete=models.CASCADE)
    risposte = models.TextField("Risposte")
    #timbro vettura ----------------
    vettura = models.SmallIntegerField("Vettura")
    linea = models.CharField("Linea", max_length=20, blank=True, default="")
    foglio = models.SmallIntegerField("Foglio", blank=True, default=0)
    owner = models.ForeignKey('auth.User', related_name='Operazione_di_verifica', on_delete=models.CASCADE)
   

    class Meta:
        ordering = ['data_registrazione']

    def save(self, *args, **kwargs):
        self.matricola_verificatore = self.owner
        super(Operazione_di_verifica, self).save(*args, **kwargs)

"""
class Questionario(models.Model):
    pass
"""