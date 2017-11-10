from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^store$', views.store, name='store'),
    url(r'^artistGalleryView/(?P<slug>[\w-]+)/$', views.artistGalleryView, name='artistGalleryView'),
    url(r'^detailed/(?P<slug>[\w-]+)/$', views.DetailedView, name='DetailedView'),
]
