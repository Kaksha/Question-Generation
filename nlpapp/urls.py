from django.urls import path, include
from . import views

urlpatterns = [
    path('get-sent', views.get_sent),
    path('get-options', views.get_options),
    path('', views.index),
]
