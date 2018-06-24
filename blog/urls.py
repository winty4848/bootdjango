from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^members/$', views.members, name='list'),
    url(r'^studying/$', views.studying, name='write'),
    url(r'^login/$', views.login, name='login'),
]
