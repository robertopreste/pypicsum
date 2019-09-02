========
pypicsum
========


.. image:: https://img.shields.io/pypi/v/pypicsum.svg
        :target: https://pypi.python.org/pypi/pypicsum

.. image:: https://img.shields.io/travis/robertopreste/pypicsum.svg
        :target: https://travis-ci.com/robertopreste/pypicsum

.. image:: https://readthedocs.org/projects/pypicsum/badge/?version=latest
        :target: https://pypicsum.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/robertopreste/pypicsum/shield.svg
     :target: https://pyup.io/repos/github/robertopreste/pypicsum/
     :alt: Updates



Simple Python API to download images from `picsum.photos`_.


* Free software: MIT license
* Documentation: https://pypicsum.readthedocs.io
* GitHub repo: https://github.com/robertopreste/pypicsum


Features
========

pypicsum can be used to download and save placeholder pictures from `picsum.photos`_, either from the command line or from inside Python.

pypicsum allows you to:

* retrieve images with a given width and height;
* retrieve a random image or specify an image id;
* retrieve grayscale images;
* retrieve images with a given level of blur;
* combine the above options to your desire.

Installation
============

**PLEASE NOTE: pypicsum only supports Python 3!**

The preferred installation method for pypicsum is using ``pip``:

.. code-block:: console

    $ pip install pypicsum

For more information, please refer to the Installation_ section of the documentation.

Usage
=====

Please refer to the Usage_ section of the documentation for an extensive usage coverage.

Command Line Interface
----------------------

To download a random image and save it locally, just run::

    pypicsum

A random 500x500 px image will be retrieved from picsum.photos and saved locally with a random name, in png format. Additional options can be used to specify width and height, image id (to retrieve a specific image instead of a random one), grayscale, blur level, path and file format to save the image.

Python Module
-------------

The ``Picsum`` class can be used to retrieve images from picsum.photos in a Python program::

    from pypicsum import Picsum
    pic = Picsum()

An empty ``Picsum()`` instance call will retrieve a random 500x500 px image, but it is possible to use additional arguments to specify more details. The ``.save()`` method allows to save the picture, optionally providing a specific path and file format::

    pic.save("my/folder/pic01", ext="jpg")

Credits
=======

This package was created with Cookiecutter_ and the `cc-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cc-pypackage`: https://github.com/robertopreste/cc-pypackage
.. _picsum.photos: https://picsum.photos
.. _Installation: https://pypicsum.readthedocs.io/en/latest/installation.html
.. _Usage: https://pypicsum.readthedocs.io/en/latest/usage.html
