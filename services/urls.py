from django.urls import path
from .views import *

app_name = 'services'

urlpatterns = [
    path('login', signIn, name='signIn'),
    path('', SuperAdmin, name='home_superAdmin'),
    path('setting-filiale/', adminAsFiliale, name='homeAdminFiliale'),

    # Page Utilisateur_filiale
    path('pole', gestpole, name='liste-pole'),
    path('processus', gestprocessus, name='liste-processus'),
    path('gestion-filiale_sAdmin/', gestFilialeSAdmin, name='gestion_filiale_admin'),
    path('gestion-filiale/', gestFiliale, name='gestion_filiale'),
    path('utilisateur_spAdmin/', gestutilisateur_spAdmin, name='liste-utilisateur_spAdmin'),
    path('utilisateur/', gestutilisateur, name='liste-utilisateur'),
    path('activite/', activite, name='activite'),


    #Page super Utilisateur
    path('gestion-filiale/', gestFiliale, name='gestion_filiale'),
    path('utilisateur/', gestutilisateur, name='liste-utilisateur'),
    path('risque-famille/', gestFiliale, name='risque_famille'),
    path('gravite-risque/', gestutilisateur, name='gravite_risque'),
    path('type-mission/', gestFiliale, name='type_mission'),
    path('corps-control/', gestutilisateur, name='corps_control'),
]
