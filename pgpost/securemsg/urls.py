from django.conf.urls import url

from . import views

app_name = 'securemsg'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addkey$', views.addkey, name='addkey'),
    url(r'^genkey$', views.genkey, name='genkey'),
    url(r'^encryptfile$', views.encryptfile, name='encryptfile'),
    url(r'^addencrypted$', views.addencrypted, name='addencrypted'),
    url(r'^sendfile_index$', views.sendfile_index, name='sendfile_index'),
    url(r'^login/(?P<confirmation>[-\w]+)/$', views.login, name='login'),
]
