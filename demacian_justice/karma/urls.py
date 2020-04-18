from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_summoner', views.get_summoner, name='get_summoner'),
]