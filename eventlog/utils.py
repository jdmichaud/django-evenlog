# -*- coding: utf-8 -*-

from django.core import serializers
import factory.django

#
# Factory
#
class EventFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = 'eventlog.Event'
