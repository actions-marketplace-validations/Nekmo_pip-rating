.. image:: https://raw.githubusercontent.com/Nekmo/pip-rating/master/logo.png
    :width: 100%

|

.. image:: https://raw.githubusercontent.com/Nekmo/pip-rating/pip-rating-badge/pip-rating-badge.svg
  :target: https://github.com/Nekmo/pip-rating/actions/workflows/pip-rating.yml
  :alt: pip-rating badge

.. image:: https://img.shields.io/github/actions/workflow/status/Nekmo/pip-rating/test.yml?style=flat-square&maxAge=2592000&branch=master
  :target: https://github.com/Nekmo/pip-rating/actions?query=workflow%3ATests
  :alt: Latest Tests CI build status

.. image:: https://img.shields.io/pypi/v/pip-rating.svg?style=flat-square
  :target: https://pypi.org/project/requirements-srating
  :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pip-rating.svg?style=flat-square
  :target: https://pypi.org/project/requirements-srating
  :alt: Python versions

.. image:: https://img.shields.io/codeclimate/maintainability/Nekmo/pip-rating.svg?style=flat-square
  :target: https://codeclimate.com/github/Nekmo/pip-rating
  :alt: Code Climate

.. image:: https://img.shields.io/codecov/c/github/Nekmo/pip-rating/master.svg?style=flat-square
  :target: https://codecov.io/github/Nekmo/pip-rating
  :alt: Test coverage

##########
pip-rating
##########

**Are the 📦 dependencies (and their dependencies) of your project secure and maintained?**


To **install 🔧 pip-rating**, run this command in your terminal (in a virtualenv preferably):

.. raw:: html

    <a href="https://xkcd.com/2347/"><img align="right" width="250px" src="https://raw.githubusercontent.com/Nekmo/pip-rating/master/docs/dependency.png" /></a>

.. code-block:: console

    $ pip install pip-rating

This is the preferred method to install pip-rating, as it will always install the most recent stable release.
If you don't have `pip <https://pip.pypa.io>`_ installed, this
`Python installation guide <http://docs.python-guide.org/en/latest/starting/installation/>`_ can guide you through
the process. 🐍 **Python 3.8-3.12** are tested and supported.
`More info in the documentation <https://docs.nekmo.org/pip-rating/installation.html>`_.

Pip-rating is a tool **to check the security and maintenance of the dependencies of your project**. It will check the
requirements of your project and **their dependencies recursively**, and will show you a rating for each of them. The
rating is based on multiple factors, like their *last release date*, the *community activity*, well-known *security
vulnerabilities* & more.

The rating for each dependency is **limited to the lowest rating of its dependencies**. For example, if you have a
package with a rating of *A*, but it depends on a package with a rating of *C*, the final rating of the package will be
*C*. This principle is based on `the XKCD comic called Dependency <https://xkcd.com/2347/>`_.
Read more about `how pip-rating works <https://docs.nekmo.org/pip-rating/overview.html>`_.

❓ Usage
========
To check the dependencies of your project (pip-rating will detect your requirements file automatically) run this
command in your project root:

.. code-block:: console

    $ pip-rating

To check the dependencies of a specific requirements file (pip-rating supports the files *requirements.txt*,
*requirements.in*, *setup.py*, *setup.cfg*, *pyproject.toml* & *Pipfile*), run this command:

.. code-block:: console

    $ pip-rating analyze-file <requirements_file>

.. image:: https://raw.githubusercontent.com/Nekmo/pip-rating/master/docs/pip-rating-text.gif
    :width: 100%
    :target: https://asciinema.org/a/596583
    :alt: pip-rating text output

By default, pip-rating shows the results in *text format*. You can also get the results in other formats like tree:

.. code-block:: console

    $ pip-rating analyze-file --format tree <requirements_file>

.. image:: https://raw.githubusercontent.com/Nekmo/pip-rating/master/docs/pip-rating-tree.gif
    :width: 100%
    :target: https://asciinema.org/a/596597
    :alt: pip-rating tree output

Pip-rating supports other formats like *json* or *only-rating*. You can see
`more examples in the documentation <https://docs.nekmo.org/pip-rating/usage.html>`_.

To analyze one or more packages, you can use the command ``pip-rating analyze-package``:

.. code-block:: console

    $ pip-rating analyze-package <package_name>[ <other_package_name>]

⚡ Github Action
===============
Pip-rating can be used as a *Github Action* to check the dependencies of your project in every commit and periodically.
To use this github action add a file like this to your project in the path ``.github/workflows/pip-rating.yml``:

.. code-block:: yaml

    # .github/workflows/pip-rating.yml
    # --------------------------------
    name: Pip-rating

    on:
      push:
        branches:
          - master
      schedule:
        - cron: '0 0 * * SUN'

    jobs:
      build:
        runs-on: ubuntu-latest
        permissions: write-all
        steps:
          - uses: actions/checkout@v2
          - name: Run pip-rating
            uses: Nekmo/pip-rating@master
            with:
              create_badge: true
              badge_style: flat-square
              badge_branch: pip-rating-badge

You can see the execution of the action in the "Actions" tab of your repository. The badge is generated in the
``pip-rating-badge`` branch, so you can access it as:

.. code-block:: text

    https://raw.githubusercontent.com/<owner>/<repository>/pip-rating-badge/pip-rating-badge.svg

For more info about the action, see the
`Github Action documentation <https://docs.nekmo.org/pip-rating/github-action.html>`_.

💡 Features
===========

* Analyze the dependencies **recursively**.
* Report of dependencies with **vulnerabilities**.
* Rating according to the **age of the project** and the **date of the last release**.
* Use of **stars**, number of **contributors**, and other criteria to define a **community rating**.
* Detect the **impersonalization** of the dependencies using cross references.
* Support for **multiple formats**: text, tree, json or only-rating.

Read more `about pip-rating in the documentation <https://docs.nekmo.org/pip-rating/>`_.

❤️ Thanks
=========
This project developed by `Nekmo <https://github.com/Nekmo>`_.

Pip-rating is licensed under the `MIT license <https://github.com/Nekmo/pip-rating/blob/master/LICENSE>`_.
