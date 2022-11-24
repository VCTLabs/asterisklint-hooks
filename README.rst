|maint|

Pre-commit hooks
================

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
      - repo: https://github.com/VCTLabs/pre-commit
        rev: <VERSION>  # Get the latest from: https://github.com/VCTLabs/pre-commit/releases
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


.. |maint| image:: https://img.shields.io/badge/maintained%20by-VCTLabs.com-blueviolet.svg
    :target: https://www.vctlabs.com/
    :alt: Maintained by VCTLabs
