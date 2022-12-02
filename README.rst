Pre-commit hooks
================

|main| |ci| |coverage| |badge|

|maint| |cov| |pylint|

|tag| |license| |python|


This repo defines Git pre-commit hooks intended for use with pre-commit_.  The
currently supported hooks are:

* asterisklint_ - check syntax of Asterisk_ PBX configuration files


.. _pre-commit: http://pre-commit.com/
.. _asterisklint: https://github.com/ossobv/asterisklint
.. _Asterisk: https://github.com/asterisk/asterisk


General Usage
-------------

In each of your repos, add a file called .pre-commit-config.yaml with the
following contents:

.. code-block:: yaml

    repos:
      - repo: https://github.com/VCTLabs/asterisklint-hooks
        rev: v0.4.3  # Get the latest from: https://github.com/VCTLabs/asterisklint-hooks/tags
        hooks:
          - id: dialplan-check

Next, have each developer:

* Install pre-commit, e.g. ``apt|brew install pre-commit``
* Run pre-commit install in the repo

That’s it! Now every time you commit a code change (``extensions.conf`` files),
the hooks in the ``hooks:`` config will execute.


Running Against All Files At Once
---------------------------------

**Example** linting all files

If you'd like to lint all of your files at once (rather than only the
changed files), you can run:

.. code-block:: bash

    $ pre-commit run dialplan-check --all-files


License
-------

This code is released under the MIT License. Please see the LICENSE file
for more details.


.. |main| image:: https://github.com/VCTLabs/asterisklint-hooks/actions/workflows/main.yml/badge.svg
    :target: https://github.com/VCTLabs/asterisklint-hooks/actions/workflows/main.yml
    :alt: Mirror Status

.. |ci| image:: https://github.com/VCTLabs/asterisklint-hooks/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/VCTLabs/asterisklint-hooks/actions/workflows/ci.yml
    :alt: CI Status

.. |coverage| image:: https://github.com/VCTLabs/asterisklint-hooks/actions/workflows/coverage.yml/badge.svg
    :target: https://github.com/VCTLabs/asterisklint-hooks/actions/workflows/coverage.yml
    :alt: Coverage Status

.. |badge| image:: https://github.com/VCTLabs/asterisklint-hooks/actions/workflows/pylint.yml/badge.svg
    :target: https://github.com/VCTLabs/asterisklint-hooks/actions/workflows/pylint.yml
    :alt: Pylint Status

.. |maint| image:: https://img.shields.io/badge/maintained%20by-VCTLabs.com-blueviolet.svg
    :target: https://www.vctlabs.com/
    :alt: Maintained by VCTLabs

.. |cov| image:: https://raw.githubusercontent.com/VCTLabs/asterisklint-hooks/badges/master/test-coverage.svg
    :target: https://github.com/VCTLabs/asterisklint-hooks/
    :alt: Test coverage

.. |pylint| image:: https://raw.githubusercontent.com/VCTLabs/asterisklint-hooks/badges/master/pylint-score.svg
    :target: https://github.com/VCTLabs/asterisklint-hooks/actions/workflows/pylint.yml
    :alt: Pylint score

.. |license| image:: https://img.shields.io/badge/license-MIT-blue
    :target: https://github.com/VCTLabs/asterisklint-hooks/blob/master/LICENSE
    :alt: License

.. |tag| image:: https://img.shields.io/github/v/tag/VCTLabs/asterisklint-hooks?color=blue&include_prereleases&label=latest%20release
    :target: https://github.com/ossobv/asterisklint/tags
    :alt: GitHub tag

.. |python| image:: https://img.shields.io/badge/python-3.7+-blue.svg
    :target: https://www.python.org/downloads/
    :alt: Python
