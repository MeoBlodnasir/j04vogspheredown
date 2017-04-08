from django.conf.urls import url

from . import views

urlpatterns = [
            url(r'^django?/$', views.django),
            url(r'^affichage?/$', views.affichage),
            url(r'^templates?/$', views.templates),
            ]
