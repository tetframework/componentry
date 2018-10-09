========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
        | |landscape| |scrutinizer| |codacy| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/componentry/badge/?style=flat
    :target: https://readthedocs.org/projects/componentry
    :alt: Documentation Status


.. |travis| image:: https://travis-ci.org/tetframework/componentry.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/tetframework/componentry

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/tetframework/componentry?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/tetframework/componentry

.. |requires| image:: https://requires.io/github/tetframework/componentry/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/tetframework/componentry/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/tetframework/componentry/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/tetframework/componentry

.. |codecov| image:: https://codecov.io/github/tetframework/componentry/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/tetframework/componentry

.. |landscape| image:: https://landscape.io/github/tetframework/componentry/master/landscape.svg?style=flat
    :target: https://landscape.io/github/tetframework/componentry/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg
    :target: https://www.codacy.com/app/tetframework/componentry
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/tetframework/componentry/badges/gpa.svg
   :target: https://codeclimate.com/github/tetframework/componentry
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/componentry.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/componentry

.. |commits-since| image:: https://img.shields.io/github/commits-since/tetframework/componentry/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/tetframework/componentry/compare/v0.0.1...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/componentry.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/componentry

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/componentry.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/componentry

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/componentry.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/componentry

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/tetframework/componentry/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/tetframework/componentry/


.. end-badges

A new Zope-inspired component registry

* Free software: GNU Affero General Public License v3 or later (AGPLv3+)

Installation
============

::

    pip install componentry

Documentation
=============


https://componentry.readthedocs.io/


Development
===========

To run the all tests run::

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
