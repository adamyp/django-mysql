# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db.transaction import atomic
from django.db.utils import DataError
from django.test import TestCase
from django.utils import six

from django_mysql.test.utils import override_mysql_variables
from django_mysql_tests.models import SizeFieldModel


# Force DataError, rather than warning
@override_mysql_variables(SQL_MODE='STRICT_TRANS_TABLES')
class SizeFieldTests(TestCase):

    @atomic
    def test_tiny_binary_max_length(self):
        # Okay
        m = SizeFieldModel(tiny_binary=six.binary_type(1) * (2**8 - 1))
        m.save()

        # Bad - Data too long
        m = SizeFieldModel(tiny_binary=six.binary_type(1) * (2**8))
        with self.assertRaises(DataError) as cm:
            m.save()
        self.assertEqual(cm.exception.args[0], 1406)

    @atomic
    def test_tiny_text_max_length(self):
        # Okay
        m = SizeFieldModel(tiny_text='a' * (2**8 - 1))
        m.save()

        # Bad - Data too long
        m = SizeFieldModel(tiny_text='a' * (2**8))
        with self.assertRaises(DataError) as cm:
            m.save()
        self.assertEqual(cm.exception.args[0], 1406)
