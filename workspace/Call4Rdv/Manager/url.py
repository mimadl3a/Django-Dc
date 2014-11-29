from django.conf.urls import url
from Manager import views


urlpatterns = [
    
    url(r'dashboardManager', views.ManagerDashboard, name="dashboardManager"),
    url(r'commercial/index', views.ManagerIndexCommercial, name="indexCommercial"),
    url(r'commercial/search', views.ManagerSearchCommercial, name="searchCommercial"),
    #url(r'commercial/create', views.ManagerCreateCommercial, name="createCommercial"),
    url(r'commercial/create', views.RegisterCommercial.as_view(), name="createCommercial"),
    #url(r'commercial/modifier/(?P<idCommercial>[0-9]+)', views.ManagerUpdateCommercial, name='updateCommercial'),
    url(r'commercial/modifier/(?P<pk>\d+)', views.UpdateRegisteredCommercial.as_view(), name='updateCommercial'),
    url(r'commercial/supprimer/(?P<idCommercial>[0-9]+)', views.ManagerDeleteCommercial, name='deleteCommercial'),
           
]