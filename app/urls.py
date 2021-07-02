from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('bingo', views.bingo),
    path('char', views.char),
]