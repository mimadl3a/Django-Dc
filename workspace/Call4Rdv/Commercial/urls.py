from django.conf.urls import url
from Commercial import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'Call4Rdv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'dashboard', views.dashboard, name="dashboard"),
    
    
    
    
    #url(r'client/liste', views.liste, name="listeClient"),
    url(r'client/index', views.ClientIndex, name="clientIndex"),
    url(r'client/search', views.ClientAjaxSearch, name="clientAjaxSearch"),
    url(r'client/modifier/(?P<idClient>[0-9]+)', views.ClientModifier, name='modifierClient'),
    
    
    
    url(r'commande/index', views.CommandeIndex, name="commandeIndex"),
    url(r'commande/create', views.CommandeCreate, name="commandeCreate"),
    url(r'commande/search', views.CommandeAjaxSearch, name="commandeAjaxSearch"),
    url(r'commande/modifier/(?P<idCommande>[0-9]+)', views.CommandeModifier, name='modifierCommande'),
    

]