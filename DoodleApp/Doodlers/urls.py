from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^^Doodlers/$', views.IndexView, name='index'),
    url(r'^Doodlers/doodle/(?P<id>[0-9]+)/$', views.DoodleView.as_view(), name='doodle'),
    url(r'^Doodlers/comment/(?P<id>[0-9]+)/$', views.comment, name='comment'),
]