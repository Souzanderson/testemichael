from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from databaseteste.api import viewsets as databaseviewsets

router = routers.DefaultRouter()
router.register(r"todos", databaseviewsets.DatabaseViewset, basename="todos")
router.register(r"vendasmes", databaseviewsets.DatabaseViewTotalVendas, basename="vendasmes")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
