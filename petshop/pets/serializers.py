# -*- coding:utf-8 -*-
from rest_framework import serializers

from pets.models import PetType


class PetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetType
        fields = '__all__'
