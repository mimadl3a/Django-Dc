from django.conf.urls import url
from Commercial import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'Call4Rdv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'step1', views.Mlogin, name="login"),
    url(r'logout', views.Mlogout, name="logout"),

]