Striper
=======

Generate sandboxed payment forms for items

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT


Authorization
--------

Login: user
Password: user

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

 To create an **superuser account**, and be able to use admin use this command

::

 $ docker-compose -f <env-file> run django python manage.py createsuperuser

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ docker-compose -f <env-file> run django pytest

Running Application
~~~~~~~~~~~~~~~~~~~

::

  $ docker-compose -f local.yml up

