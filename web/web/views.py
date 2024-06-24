from django.shortcuts import *
from .models import Capteurs, Donnees
from .forms import CapteursForm
from . import models
from django.utils.dateparse import parse_datetime
import csv  

def index(request):
    return render(request, 'web/index.html')

def donnee(request):
    capteur_id = request.GET.get('capteur_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    donnees = Donnees.objects.all()

    if capteur_id:
        donnees = donnees.filter(CapteurID=capteur_id)
    if start_date and end_date:
        donnees = donnees.filter(Timestamp__range=[start_date, end_date])
    elif start_date:
        donnees = donnees.filter(Timestamp__gte=start_date)
    elif end_date:
        donnees = donnees.filter(Timestamp__lte=end_date)

    if 'export_csv' in request.GET:
        return export_csv(request, Donnees, donnees)

    return render(request, 'web/donnee.html', {'Donnees': donnees})

def capteur(request):
    nom = request.GET.get('nom')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    capteurs = Capteurs.objects.all()

    if nom:
        capteurs = capteurs.filter(Q(Nom__icontains=nom) | Q(Id=nom))
    if start_date and end_date:
        capteurs = capteurs.filter(Date__range=[start_date, end_date])
    elif start_date:
        capteurs = capteurs.filter(Date__gte=start_date)
    elif end_date:
        capteurs = capteurs.filter(Date__lte=end_date)

    if 'export_csv' in request.GET:
        return export_csv(request, Capteurs, capteurs)

    return render(request, 'web/capteur.html', {'Capteurs': capteurs})

def editname(request, Id):
    Capteur = models.Capteurs.objects.get(Id=Id)
    form = CapteursForm(instance=Capteur)
    return render(request, 'web/editname.html', {'form': form, 'Capteur': Capteur})

def editemplacement(request, Id):
    Capteur = models.Capteurs.objects.get(Id=Id)
    form = CapteursForm(instance=Capteur)
    return render(request, 'web/editemplacement.html', {'form': form, 'Capteur': Capteur})

def traitementname(request, id):
    Capteur = models.Capteurs.objects.get(Id=id)
    lform = CapteursForm(request.POST, instance=Capteur)
    if lform.is_valid():
        Capteur = lform.save()
        return HttpResponseRedirect("/capteur")
    else:
        return render(request, 'web/editname.html', {'form': lform, 'Capteur': Capteur})
    
def traitementemplacement(request, id):
    Capteur = models.Capteurs.objects.get(Id=id)
    lform = CapteursForm(request.POST, instance=Capteur)
    if lform.is_valid():
        Capteur = lform.save()
        return HttpResponseRedirect("/capteur")
    else:
        return render(request, 'web/editemplacement.html', {'form': lform, 'Capteur': Capteur})
    

def export_csv(request, model, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    writer = csv.writer(response)
    headers = [field.name for field in model._meta.fields]
    writer.writerow(headers)

    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in headers])

    return response             

