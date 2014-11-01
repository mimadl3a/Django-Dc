from django.conf.urls import include, url
from django.contrib import admin
from Commercial import urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'Call4Rdv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^commercial/', include(urls)),

    url(r'^admin/', include(admin.site.urls)),
]
