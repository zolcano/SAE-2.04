from django import forms
from . import models
from .models import Capteurs, Donnees
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

class CapteursForm(ModelForm):
    class Meta:
        model = Capteurs
        fields = ['Id', 'Nom', 'Piece', 'Emplacement', 'Date']
        label = {
            'Id': 'clé primaire',
            'Nom': 'Nom du capteur',
            'Piece': 'Piece du capteur',
            'Emplacement' : 'Emplacement du capteur',
            'Date': 'Date de la prise d information',
            }
        
class DonneesForm(ModelForm):
    class Meta:
        model = Donnees
        fields = ['Id', 'CapteurID', 'Timestamp', 'Valeur']
        label = {
            'Id': 'clé primaire',
            'CapteurID': 'Id du capteur',
            'Timestamp': 'Date de la prise de température',
            'Valeur': 'Température mesurée',
            }

