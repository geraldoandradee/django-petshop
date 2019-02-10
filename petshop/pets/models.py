# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class PetType(models.Model):
    """
    Model represent the type of the pet. Like: Dog, Cat, Rabbit..etc
    """

    pet_type = models.CharField(max_length=255, null=True, blank=True,
                                verbose_name="Type of the pet")
    is_active = models.BooleanField(default=True,
                                    verbose_name="Is pet type active")
    created = models.DateTimeField(null=True, auto_now_add=True)
    modified = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = "Pet Types"
        app_label = 'pets'

    def __str__(self):
        return '{}'.format(self.pet_type)


class PetDetails(models.Model):
    """
    Model Represent the details of the pet. Like: pet's name, dob etc..
    """

    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True,
                              blank=True, related_name="pet_owner")
    name = models.CharField(max_length=255, null=True, blank=True,
                            verbose_name="Name of the pet")
    dob = models.DateField(null=True, blank=True,
                           verbose_name="Date of birth of pet")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = "Pet Details"
        app_label = 'pets'

    def __str__(self):
        return '{}'.format(self.name if self.name else self.pk)
