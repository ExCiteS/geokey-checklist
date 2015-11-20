.. image:: https://img.shields.io/pypi/v/geokey-checklist.svg
    :alt: PyPI Package
    :target: https://pypi.python.org/pypi/geokey-checklist

.. image:: https://img.shields.io/travis/ExCiteS/geokey-checklist/master.svg
    :alt: Travis CI Build Status
    :target: https://travis-ci.org/ExCiteS/geokey-checklist

.. image:: https://img.shields.io/coveralls/ExCiteS/geokey-checklist/master.svg
    :alt: Coveralls Test Coverage
    :target: https://coveralls.io/r/ExCiteS/geokey-checklist

geokey-checklist
================

Install
-------

Install the extension from PyPI:

.. code-block:: console

    pip install geokey-checklist

Or from cloned repository:

.. code-block:: console

    cd geokey-checklist
    pip install -e .

Add the package to installed apps:

.. code-block:: console

    INSTALLED_APPS += (
        ...
        'geokey_checklist',
    )

Migrate the models into the database:

.. code-block:: console

    python manage.py migrate geokey_checklist

Copy static files:

.. code-block:: console

    python manage.py collectstatic

You're now ready to go!

Test
----

Run tests:

.. code-block:: console

    python manage.py test geokey_checklist

Check code coverage:

.. code-block:: console

    coverage run --source=geokey_checklist manage.py test geokey_checklist
    coverage report -m --omit=*/tests/*,*/migrations/*
