#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import requests
from typing import Optional, Union
from .helpers import random_string


class Picsum:
    """Class used to retrieve an image from Picsum and save it locally.

    :param int width: width of the image (default: 500)
    :param Optional[int] height: height of the image, if not provided
    returns a square image (default: None)
    :param Optional[int] image: return a specific image instead of a
    random one (default: None)
    :param bool grayscale: return the grayscale version of the image
    (default: False)
    :param bool blurred: return the blurred version of the image
    (default: False)
    :param Optional[str] gravity: gravity crop of the image, accepts one
    of 'north', 'east', 'south', 'west', 'center' (default: None)

    # random 500 x 500 px image
    >>> Picsum()
    # random 500 x 800 px image
    >>> Picsum(500, 800)
    """

    def __init__(self,
                 width: int = 500,
                 height: Optional[int] = None,
                 image: Optional[int] = None,
                 grayscale: bool = False,
                 blurred: bool = False,
                 gravity: Optional[str] = None):
        self.width = width
        self.height = height
        self.image = image
        self.grayscale = grayscale
        self.blurred = blurred
        self.gravity = gravity
        self._request_call = requests.get(self.request_url)
        self._filename = ""

    @property
    def request_url(self) -> str:
        """Return the url to call.

        Return the url used retrieve the image from Picsum.
        :return: str
        """
        base_url = "https://picsum.photos"
        if self.grayscale:
            base_url += "/g"
        base_url += "/{}".format(self.width)
        if self.height:
            base_url += "/{}".format(self.height)
        if self.image:
            if not isinstance(self.image, int):
                raise ValueError("Please provide a integer number.")
            base_url += "?/image={}".format(self.image)
        else:
            base_url += "/?random"
        if self.blurred:
            base_url += "/?blur"
        if self.gravity:
            if self.gravity not in ["north", "east", "south", "west",
                                    "center"]:
                raise ValueError("Please provide either 'north', 'east', " 
                                 "'south', 'west' or 'center'. ")
            base_url += "/?gravity={}".format(self.gravity)

        return base_url

    @property
    def pic(self) -> bytes:
        """Return he retrieved image bytes.

        Return the actual content of the image, which can be saved as png.
        :return: bytes
        """
        return self._request_call.content

    @property
    def url(self) -> str:
        """Return the image url.

        Return the url used to retrieve the image (after parsing by Picsum).
        :return: str
        """

        return self._request_call.url

    @property
    def filename(self) -> str:
        """Return the output file name.

        Return the filename to which the image was saved.
        :return: str
        """
        return self._filename

    def save(self,
             path: Optional[str] = None,
             ext: str = "png") -> bool:
        """Save the retrieved image to a png file.

        Save the image retrieved from Picsum to a file in png format. If
        no path is provided, or if path is a directory, a random filename
        will be created, and care will be taken to ensure that no files
        with the same name already exist. Otherwise, the image will be
        saved to the given filename (automatically appending the .png
        suffix).
        :param Optional[str] path: path/filename to save the image
        :param str ext: output file extension (default: png)
        :return: True
        """
        if ext not in ["png", "jpeg", "jpg"]:
            raise ValueError("Filetype not allowed." 
                             "Please provide either 'png', 'jpeg' or 'jpg'.")
        rnd_name = "{}.{}".format(random_string(), ext)
        if path:
            if os.path.isdir(path):
                while os.path.isfile(os.path.join(path, rnd_name)):
                    rnd_name = "{}.{}".format(random_string(), ext)
                self._filename = os.path.join(path, rnd_name)
            elif os.path.isfile(path):
                raise FileExistsError("File {} already exists!".format(path),
                                      "Please provide a different filename.")
            else:
                self._filename = path
        else:
            while os.path.isfile(rnd_name):
                rnd_name = "{}.{}".format(random_string(), ext)
            self._filename = rnd_name

        with open(self._filename, "wb") as f:
            f.write(self.pic)

        return True

