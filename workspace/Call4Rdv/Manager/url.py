from django.conf.urls import url
from Manager import views


urlpatterns = [
    
    url(r'dashboard', views.ManagerDashboard, name="dashboard"),
    url(r'commercial/index', views.ManagerIndexCommercial, name="indexCommercial"),
    url(r'commercial/search', views.ManagerSearchCommercial, name="searchCommercial"),
    url(r'commercial/create', views.ManagerCreateCommercial, name="createCommercial"),
    url(r'commercial/modifier/(?P<idCommercial>[0-9]+)', views.ManagerUpdateCommercial, name='updateCommercial'),
    url(r'commercial/supprimer/(?P<idCommercial>[0-9]+)', views.ManagerDeleteCommercial, name='deleteCommercial'),
       
]