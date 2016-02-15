from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<creation_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^requestnewcreation/$', views.requestnewcreation, name='requestnewcreation')
]
