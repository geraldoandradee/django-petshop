# -*- coding: utf-8 -*-
import django_filters

from rest_framework import viewsets

from pets.models import PetType
from pets.serializers import PetTypeSerializer


class PetTypeViewSet(viewsets.ModelViewSet):
    filter_fields = ('pet_type', 'is_active')
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    queryset = PetType.objects.all()
    serializer_class = PetTypeSerializer
