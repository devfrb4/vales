from django.conf.urls import url
from . import views as aViews

urlpatterns = [
    url(r'^login/$', aViews.Login.as_view(), name='login'),
    url(r'^signup/$', aViews.Register.as_view(), name='signup'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login'}, name='logout')
]