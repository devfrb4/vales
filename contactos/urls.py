from django.conf.urls import url
from . import views as cViews

urlpatterns = [
    url(r'^$', cViews.get_contactos, name='get_contactos'),
	url(r'^new/$', cViews.PersonView.as_view(), name='person-new')
]