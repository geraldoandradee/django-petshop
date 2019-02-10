# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from pets.api import PetTypeViewSet

admin.autodiscover()

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'pets', PetTypeViewSet)

urlpatterns = [
    url(r'/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
