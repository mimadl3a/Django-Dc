from django.conf.urls import url
from Manager import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'Call4Rdv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'Managerstep1', views.Managerlogin, name="Managerlogin"),
    url(r'Managerlogout', views.Managerlogout, name="Managerlogout"),

]