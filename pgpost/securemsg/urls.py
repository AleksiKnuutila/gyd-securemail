from django.conf.urls import url

from . import views

app_name = 'securemsg'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addkey$', views.addkey, name='addkey'),
    url(r'^genkey$', views.genkey, name='genkey'),
    url(r'^datarequest/(?P<slug>[\w-]+)/$', views.datarequest, name='datarequest')
]