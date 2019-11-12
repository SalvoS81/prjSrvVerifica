# Generated by Django 2.2.7 on 2019-11-11 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Operazione_di_verifica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricola_verificatore', models.CharField(max_length=5, verbose_name='Matricola del verificatore')),
                ('data_registrazione', models.DateTimeField(auto_now_add=True, verbose_name='Data di registrazione')),
                ('risposte', models.TextField(verbose_name='Risposte')),
                ('vettura', models.SmallIntegerField(verbose_name='Vettura')),
                ('linea', models.CharField(max_length=20, verbose_name='Linea')),
                ('foglio', models.SmallIntegerField(verbose_name='Foglio')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Operazione_di_verifica', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['data_registrazione'],
            },
        ),
    ]