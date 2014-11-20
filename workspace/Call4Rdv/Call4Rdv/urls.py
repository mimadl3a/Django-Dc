from django.conf.urls import include, url
from django.contrib import admin
from Commercial import urls, login_urls
from Manager import url as urls_manager
from Manager import login_urls as urls_manager_login


handler404 = 'Manager.views.custom_404'
handler500 = 'Manager.views.custom_500'

urlpatterns = [
    # Examples:
    # url(r'^$', 'Call4Rdv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    
    url(r'^login/', include(login_urls)),
    
    url(r'^Managerlogin/', include(urls_manager_login)),
    
    url(r'^commercial/', include(urls)),
    
    url(r'^manager/', include(urls_manager)),

    url(r'^admin/', include(admin.site.urls)),
]
