from django.conf.urls import url

from .views import ListAffair, DetailAffair

urlpatterns = [
    url(r'^affair/$', ListAffair.as_view(), name='lista-affair' ),
    url(r'^affair/(?P<pk>[0-9]+)/$', DetailAffair.as_view(), name='detail-affair' ),
]