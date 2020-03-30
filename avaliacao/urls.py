from django.conf.urls import url
from django.contrib import admin

from . import views

import dashboard

urlpatterns = [
    url(r'^avaliacao', views.avaliacao, name='avaliacao'),
    url(r'^', dashboard.views.index, name='home'),
]
