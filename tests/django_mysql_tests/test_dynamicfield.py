# -*- coding:utf-8 -*-
from unittest import expectedFailure, skipIf, SkipTest

import django
from django.db import connection
from django.test import TestCase

from django_mysql_tests.models import DynamicModel


@skipIf(django.VERSION <= (1, 8), "Requires Expressions from Django 1.8+")
class TestSaveLoad(TestCase):

    @classmethod
    def setUpClass(cls):
        if not (
            connection.is_mariadb and
            connection.mysql_version > (10, 0, 1)
        ):
            raise SkipTest("Dynamic Columns require MariaDB 10.0.1+")
        super(TestSaveLoad, cls).setUpClass()

    def test_simple_key_value(self):
        self.assertEqual(list(DynamicModel.objects.all()), [])
        s = DynamicModel.objects.create()
        self.assertEqual(s.attrs, {})
        s = DynamicModel.objects.get()

        self.assertEqual(s.attrs, {})

        s.attrs['key'] = 'value!'
        s.attrs['2key'] = 23
        s.save()

        s = DynamicModel.objects.get()
        self.assertEqual(s.attrs, {'key': 'value!', '2key': 23})

        del s.attrs['key']
        s.save()

        s = DynamicModel.objects.get()
        self.assertEqual(s.attrs, {'2key': 23})

        del s.attrs['2key']
        s.save()
        s = DynamicModel.objects.get()
        self.assertEqual(s.attrs, {})

    @expectedFailure
    def test_create(self):
        # Broken until https://code.djangoproject.com/ticket/24509 is fixed
        DynamicModel.objects.create(attrs={
            'a': 'value'
        })
        s = DynamicModel.objects.get()
        self.assertEqual(s.attrs['a'], 'value')
