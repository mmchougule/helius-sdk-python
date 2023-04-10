========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions|
        | |codecov|
.. |docs| image:: https://readthedocs.org/projects/helius-sdk-python/badge/?style=flat
    :target: https://helius-sdk-python.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/mmchougule/helius-sdk-python/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/mmchougule/helius-sdk-python/actions

.. |codecov| image:: https://codecov.io/gh/mmchougule/helius-sdk-python/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/mmchougule/helius-sdk-python

.. |version| image:: https://img.shields.io/pypi/v/helius-sdk.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/helius-sdk

.. |wheel| image:: https://img.shields.io/pypi/wheel/helius-sdk.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/helius-sdk

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/helius-sdk.svg
    :alt: Supported versions
    :target: https://pypi.org/project/helius-sdk

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/helius-sdk.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/helius-sdk

.. |commits-since| image:: https://img.shields.io/github/commits-since/mmchougule/helius-sdk-python/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/mmchougule/helius-sdk-python/compare/v0.0.0...main



.. end-badges

WIP

Installation
============

::

    pip install helius-sdk

You can also install the in-development version with::

    pip install https://github.com/mmchougule/helius-sdk-python/archive/main.zip



Examples
========

Get transaction details

    >>> from helius_sdk.transaction import Transaction
    >>> t = Transaction(api_key="api_key", tx_address="").get()
    >>> t.shape

Get nft sales

    >>> from helius_sdk.event import Sale
    >>> sale = Sale(api_key="api_key", col_address="").get()
    >>> sale.shape

Documentation
=============


https://helius-sdk-python.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
