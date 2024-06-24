from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('donnee/',views.donnee, name='donnee'),
    path('capteur/',views.capteur, name='capteur'),
    path('editname/<int:Id>/', views.editname, name='editname'),
    path('traitementname/<int:id>/', views.traitementname, name='traitementname'),
    path('editemplacement/<int:Id>/', views.editemplacement, name='editemplacement'),
    path('traitementemplacement/<int:id>/', views.traitementemplacement, name='traitementemplacement'),
    
]
