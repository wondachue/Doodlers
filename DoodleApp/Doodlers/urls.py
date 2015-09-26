from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<title>[0-9]+)/doodle/$', views.doodle, name='doodle'),
    url(r'^(?P<title>[0-9]+)/comment/$', views.comment, name='comment'),
]