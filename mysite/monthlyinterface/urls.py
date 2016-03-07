from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<creation_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<creation_id>[0-9]+)/fork$', views.fork, name='fork'),
    url(r'^specificlist/$', views.specificlist, name='specificlist'),
    url(r'^requestnewcreation/$', views.requestnewcreation, name='requestnewcreation'),
    url(r'^requestednewcreation/$', views.requestednewcreation, name='requestednewcreation')
]
