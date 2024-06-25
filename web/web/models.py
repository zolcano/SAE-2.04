from django.db import models

class Capteurs(models.Model):
    Id = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=250, blank=True, null=True)
    Piece = models.CharField(max_length=50, unique=True, blank=True, null=True)
    Emplacement = models.CharField(max_length=50, blank=True, null=True)
    Date = models.CharField(max_length=50, blank=True, null=True)
        
    def __str__(self):
        return f"{self.Nom} {self.Piece} {self.Emplacement} {self.Date}"
        
    class Meta:
        db_table = "Capteur"
    
class Donnees(models.Model):
    Id = models.AutoField(primary_key=True)
    CapteurID = models.CharField(max_length=50, unique=True, blank=True, null=True)
    Timestamp = models.CharField(max_length=50, blank=True, null=True)
    Valeur = models.CharField(max_length=50, blank=True, null=True)
        
    def __str__(self):
        return f"{self.CapteurID} {self.Timestamp} {self.Valeur}"
        
    class Meta:
        db_table = "Donnees"

