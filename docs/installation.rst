Installation
============

Pip/virtualenv
--------------

Create a new virtual environment, and install the development version of bentso:

.. code-block:: bash

    pip install https://github.com/BONSAMURAIS/bentso/archive/master.zip

Conda
-----

Create a new Conda environment:

.. code-block:: bash

    conda create -n bentso -y -q -c conda-forge -c cmutel python=3.7 bentso

Developers
----------

Create a new Conda environment:

.. code-block:: bash

    conda create -n bentso -y -q -c conda-forge python=3.7 requests pytz pandas beautifulsoup4 pytest pytest-env appdirs docopt twine jupyter ipython

Clone `bentso from Github <https://github.com/BONSAMURAIS/bentso>`__, and in the bentso directory run:

.. code-block:: bash

    pip install -e .
