from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista, name='lista'),
    url(r'^/(?P<pk>\d+)/$', views.ver_contato, name='ver_contato'),
]