from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Doodlers/doodle/(?P<id>[0-9]+)/$', views.doodle, name='doodle'),
    url(r'^Doodlers/comment/(?P<id>[0-9]+)/$', views.comment, name='comment'),
]