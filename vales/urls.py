from django.conf.urls import patterns, include, url
from django.contrib import admin
from contactos import views as contacto_views
from api import views as api_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'contactos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^contactos/', include('contactos.urls', namespace='contactos')),
    url(r'^contacts/$', api_views.PersonViewList.as_view(), name='list-contactos'),
    url(r'^contacts/(?P<pk>[0-9]+)/$', api_views.PersonViewDetail.as_view(), name='detail-contactos'),
)


urlpatterns = format_suffix_patterns(urlpatterns)