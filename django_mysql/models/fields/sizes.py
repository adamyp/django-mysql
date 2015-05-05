from django.db.models import BinaryField, SubfieldBase, TextField
from django.utils import six

__all__ = (
    'TinyBinaryField', 'BasicBinaryField', 'MediumBinaryField',
    'TinyTextField', 'BasicTextField', 'MediumTextField',
)


# Django's BinaryField is LONGBLOB

class TinyBinaryField(six.with_metaclass(SubfieldBase, BinaryField)):
    def db_type(self, connection):
        return 'TINYBLOB'


class BasicBinaryField(six.with_metaclass(SubfieldBase, BinaryField)):
    def db_type(self, connection):
        return 'BLOB'


class MediumBinaryField(six.with_metaclass(SubfieldBase, BinaryField)):
    def db_type(self, connection):
        return 'MEDIUMBLOB'


# Django's TextField is LONGTEXT

class TinyTextField(six.with_metaclass(SubfieldBase, TextField)):
    def db_type(self, connection):
        return 'TINYTEXT'


class BasicTextField(six.with_metaclass(SubfieldBase, TextField)):
    def db_type(self, connection):
        return 'TEXT'


class MediumTextField(six.with_metaclass(SubfieldBase, TextField)):
    def db_type(self, connection):
        return 'MEDIUMTEXT'
