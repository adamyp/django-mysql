============
Django MySQL
============

.. image:: https://badge.fury.io/py/django-mysql.png
    :target: http://badge.fury.io/py/django-mysql

.. image:: https://travis-ci.org/adamchainz/django-mysql.png?branch=master
        :target: https://travis-ci.org/adamchainz/django-mysql

.. image:: https://coveralls.io/repos/adamchainz/django-mysql/badge.svg
        :target: https://coveralls.io/r/adamchainz/django-mysql

.. image:: https://pypip.in/d/django-mysql/badge.png
        :target: https://pypi.python.org/pypi/django-mysql

.. image:: https://readthedocs.org/projects/django-mysql/badge/?version=latest
        :target: http://django-mysql.readthedocs.org/en/latest/


.. figure:: https://raw.github.com/adamchainz/django-mysql/master/docs/images/dolphin-pony.png
   :alt: The dolphin-pony - proof that cute + cute = double cute.

..

    | The dolphin-pony - proof that cute + cute = double cute.


Django-MySQL is a non-inventively named package that helps you use some
MySQL/MariaDB-specific features in the world of Django.


What kind of features?
----------------------

Includes:

* ``QuerySet`` extensions - 'smart' iteration, ``approx_count`` for quick
  estimates of ``count()``, quick ``pt-visual-explain`` of the underlying
  query
* Model fields for storing lists and sets in comma-separated strings, with the
  ability to query them
* ORM expressions for MySQL-specific functions
* A new cache backend that makes use of MySQL's upserts and does compression
* Handler API for quicker-than-SQL reads using the 'NoSQL' HANDLER commands
* Status variable inspection and utility methods
* Named locks for easy locking of e.g. external resources

To see them all, check out the exposition at
http://django-mysql.readthedocs.org/en/latest/exposition.html .

Requirements
------------

Tested with all combinations of:

* Python: 2.7, 3.4
* Django: 1.7, 1.8
* MySQL: 5.5, 5.6 / MariaDB: 5.5, 10.0, 10.1
* mysqlclient: 1.3.6 (Python 3 compatible version of ``MySQL-python``)

Any combination of these should be good, and also ``MySQL-python`` should work
since it's just an older version of ``mysqlclient``.
