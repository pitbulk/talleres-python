from django.conf.urls import patterns, include, url
from django.contrib import admin
from mongoadmin import site
from rest_framework_mongoengine import routers
from apirest.viewsets import AccionViewSet, UserViewSet#, AccionList, AccionDetail

admin.autodiscover()

router = routers.MongoDefaultRouter()
router.register(r'acciones', AccionViewSet)
router.register(r'users', UserViewSet)

urlpatterns = patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(site.urls)),

    #url(r'^apinonrel/acciones/$', AccionList.as_view()),
    #url(r'^apinonrel/acciones/(?P<id>[0-9a-z]+)/$', AccionDetail.as_view()),
)
