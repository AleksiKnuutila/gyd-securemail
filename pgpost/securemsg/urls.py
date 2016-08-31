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
    url(r'^decrypt_index$', views.decrypt_index, name='decrypt_index'),
    url(r'^json_get_publickey', views.json_get_publickey, name='json_get_publickey'),
    url(r'^json_get_datareq', views.json_get_datareq, name='json_get_datareq'),
    url(r'^json_addencrypted', views.json_addencrypted, name='json_addencrypted'),
]
