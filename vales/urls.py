from django.conf.urls import patterns, include, url
from django.contrib import admin
from contactos import views as contacto_views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'contactos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^contactos/', include('contactos.urls', namespace='contactos'))
)
