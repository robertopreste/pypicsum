=====
Usage
=====

Command Line Interface
======================

To download a random image and save it locally, just run::

    pypicsum

A random 500x500 px image will be retrieved from picsum.photos and saved locally with a random name, in png format. Additional options can be used to specify width and height, image id (to retrieve a specific image instead of a random one), grayscale, blur level, path and file format to save the image.

Python Module
=============

The ``Picsum`` class can be used to retrieve images from picsum.photos in a Python program::

    from pypicsum import Picsum
    pic = Picsum()

An empty ``Picsum()`` instance call will retrieve a random 500x500 px image, but it is possible to use additional arguments to specify more details. The ``.save()`` method allows to save the picture, optionally providing a specific path and file format::

    pic.save("my/folder/pic01", ext="jpg")
