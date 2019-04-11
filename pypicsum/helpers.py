#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import random as rand
import requests
from string import ascii_letters, digits
from typing import Optional


def random_string(length: int = 12) -> str:
    """Create a random string of the given length.

    Return a random alphanumeric string of the given length, which will
    be used for the image filename.
    :param int length: desired length of the random string (default: 6)
    :return: str
    """
    source = ascii_letters + digits

    return "".join([rand.choice(source) for _ in range(length)])


class Picsum:
    def __init__(self,
                 width: int = 500,
                 height: Optional[int] = None,
                 random: bool = True,
                 grayscale: bool = False,
                 blurred: bool = False,
                 gravity: Optional[str] = None):
        self.width = width
        self.height = height
        self.random = random
        self.grayscale = grayscale
        self.blurred = blurred
        self.gravity = gravity
        self._image_call = requests.get(self.request_url)

    @property
    def request_url(self) -> str:
        """
        Return the url used retrieve the image from Picsum.
        :return: str
        """
        base_url = "https://picsum.photos"
        if self.grayscale:
            base_url += "/g"
        base_url += "/{}".format(self.width)
        if self.height:
            base_url += "/{}".format(self.height)
        if self.random:
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
    def image(self) -> bytes:
        """
        Return the actual content of the image, which can be saved as png.
        :return: bytes
        """

        return self._image_call.content

    @property
    def url(self) -> str:
        """
        Return the url used to retrieve the image (after parsing by Picsum).
        :return: str
        """

        return self._image_call.url

    def save(self, path: Optional[str] = None) -> None:
        """Save the retrieved image to a png file.

        Save the image retrieved from Picsum to a file in png format. If
        no path is provided, or if path is a directory, a random filename
        will be created, and care will be taken to ensure that no files
        with the same name already exist. Otherwise, the image will be
        saved to the given filename (automatically appending the .png
        suffix).
        :param Optional[str] path: path/filename to save the image
        :return: None
        """
        # TODO: add option to specify desired image format
        rnd_name = "{}.png".format(random_string())
        if path:
            if os.path.isdir(path):
                while os.path.isfile(os.path.join(path, rnd_name)):
                    rnd_name = "{}.png".format(random_string())
                filename = os.path.join(path, rnd_name)
            elif os.path.isfile(path):
                raise FileExistsError("File {} already exists!".format(path),
                                      "Please provide a different filename.")
            else:
                filename = path
        else:
            while os.path.isfile(rnd_name):
                rnd_name = "{}.png".format(random_string())
            filename = rnd_name

        with open(filename, "wb") as f:
            f.write(self.image)

        return




