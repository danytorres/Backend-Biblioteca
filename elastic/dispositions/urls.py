from django.conf.urls import url

from .views import ListDisposition, DetailDisposition

urlpatterns = [
    url(r'^disposition/$', ListDisposition.as_view(), name='lista-disposition' ),
    url(r'^disposition/(?P<pk>[0-9]+)/$', DetailDisposition.as_view(), name='detail-disposition' ),
]