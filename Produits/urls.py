from django.urls import path
from .views import * 
from django.conf import settings
from django.conf.urls.static import static

from . import views  # ✅ ceci est indispensable

from . import views


urlpatterns = [
    path('',acc,name='acc'),

    path('produit/', Affichage.as_view(), name='home'),
    path('ajout/', AjoutProduits.as_view(), name='ajout'),
    # path('modification/<int:id>/', modifier,name='modifier'),
    # pour url de IA

    path('ia/', views.ia_assistant, name='ia_assistant'), 

    path('ia/', views.ia_assistant, name='ia_assistant'),

    path('modication/<int:pk>/', update_donnees.as_view(), name='modifier'),
    # path('supprimer/<int:id>/', supprimer, name="supprimer"),
#    path ('detail/<int:id>/', detail,name='detail'),
    path('details/<int:pk>/', edit.as_view(),name='details'),
    
    path('delete/<int:pk>/', delete.as_view(),name='delete'),

    path('recherche/', recherche, name='recherche'),

    path('ajoutvente/<int:id>/', VenteProduits, name='ajoutvente'),
    path('saverecu/<int:id>/', SaveRecu, name='saverecu'),
    path('facture/<int:sale_id>/', Facture, name='facture'),
    # path('ajout/',ajout_donnees,name='ajout'),
   # autres urls...
    path('notifications/', notifications_view, name='notifications'),
    path('historique-ventes/', views.historique_ventes, name='historique_ventes'),

    path('statistiques/', statistiques_view, name='statistiques'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








