# -*- coding:utf-8 -*-
from __future__ import absolute_import

import json

from django.db.models import Field, SubfieldBase
from django.utils import six

from django_mysql.models.functions import ColumnCreate

__all__ = ('DynamicField',)


class DynamicField(six.with_metaclass(SubfieldBase, Field)):
    def db_type(self, connection):
        return 'mediumblob'

    def to_python(self, value):
        if isinstance(value, (six.string_types, six.binary_type)):
            if not value:
                return {}
            return json.loads(value.decode('utf8'))
        return value

    def get_prep_value(self, value):
        if value is None:
            return value
        if not value:
            return six.binary_type()
        return ColumnCreate(value)

    def get_internal_type(self):
        return 'BinaryField'

    def select_format(self, compiler, sql, params):
        return "COLUMN_JSON(%s)" % sql, params

    def deconstruct(self):
        name, path, args, kwargs = super(DynamicField, self).deconstruct()
        path = 'django_mysql.models.%s' % self.__class__.__name__
        return name, path, args, kwargs
