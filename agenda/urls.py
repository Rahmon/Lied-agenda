from django.conf.urls import url, include
from rest_framework import routers
from agenda.webservice import views

router = routers.DefaultRouter()
router.register(r'contato', views.ContatoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'site', include('agenda.frontend.urls')),
]