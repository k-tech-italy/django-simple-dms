from datetime import date

import factory
import faker
from django.utils.text import slugify
from factory.base import FactoryMetaClass

from django_simple_dms.models import DocumentTag

factories_registry = {}


class AutoRegisterFactoryMetaClass(FactoryMetaClass):
    def __new__(cls, class_name, bases, attrs):
        new_class = super().__new__(cls, class_name, bases, attrs)
        factories_registry[new_class._meta.model] = new_class
        return new_class


class AutoRegisterModelFactory(factory.django.DjangoModelFactory, metaclass=AutoRegisterFactoryMetaClass):
    pass


def get_factory_for_model(_model):
    class Meta:
        model = _model

    if _model in factories_registry:
        return factories_registry[_model]
    return type(f'{_model._meta.model_name}AutoFactory', (AutoRegisterModelFactory,), {'Meta': Meta})


class DocumentTagFactory(factory.django.DjangoModelFactory):

    id = factory.Sequence(lambda n: f't_{n}')

    class Meta:
        model = DocumentTag