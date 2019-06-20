#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import random
import requests
from string import ascii_letters, digits
from typing import Optional


class Picsum:
    """Class used to retrieve an image from Picsum and save it locally.

    Once retrieved, the image can be shown interactively using
    IPython.display.Image(), or it can be saved locally using
    Picsum.save().

    :param int width: width of the image (default: 500)

    :param Optional[int] height: height of the image, if not provided
        returns a square image (default: None)

    :param Optional[int] id_: return a specific image instead of a
        random one (default: None)

    :param bool grayscale: return the grayscale version of the image
        (default: False)

    :param Optional[int] blur: return a blurred version of the image
        and select a blurring value between 1 and 10 (default: None)

    # random 500 x 500 px image
    >>> Picsum()
    # random 500 x 800 px image
    >>> Picsum(500, 800)
    """

    def __init__(self,
                 width: int = 500,
                 height: Optional[int] = None,
                 id_: Optional[int] = None,
                 grayscale: bool = False,
                 blur: Optional[int] = None):
        self.width = width
        self.height = height
        self.id_ = id_
        self.grayscale = grayscale
        self.blur = blur
        self._request_call = requests.get(self.request_url)
        self._filename = ""

    @property
    def request_url(self) -> str:
        """Return the url to call.

        Return the url used retrieve the image from Picsum.

        :return: str
        """
        base_url = "https://picsum.photos"
        if self.id_ or self.id_ == 0:
            if not isinstance(self.id_, int):
                raise ValueError("Please provide an integer number.")
            base_url += "/id/{}".format(self.id_)
        base_url += "/{}".format(self.width)
        if self.height:
            base_url += "/{}".format(self.height)
        if self.grayscale:
            base_url += "/?grayscale"
        if self.blur:
            if self.grayscale:
                base_url += "&blur"
            else:
                base_url += "/?blur"
            if int(self.blur) not in range(1, 11):
                raise ValueError("Please provide an integer number "
                                 "between 1 and 10.")
            base_url += "={}".format(self.blur)

        return base_url

    @property
    def pic(self) -> bytes:
        """Return the retrieved image bytes.

        Return the actual content of the image, which can be saved as png.

        :return: bytes
        """
        return self._request_call.content

    @property
    def url(self) -> str:
        """Return the Picsum image url.

        Return the url used to retrieve the image (after parsing by Picsum).

        :return: str
        """

        return self._request_call.url

    @property
    def filename(self) -> str:
        """Return the output file name.

        Return the filename to which the image was (or will be) saved.

        :return: str
        """
        return self._filename

    @staticmethod
    def random_string(length: int = 12) -> str:
        """Create a random string of the given length.

        Return a random alphanumeric string of the given length, which will
        be used for the image filename.

        :param int length: desired length of the random string (default: 12)

        :return: str
        """
        source = ascii_letters + digits

        return "".join([random.choice(source) for _ in range(length)])

    def save(self,
             path: Optional[str] = None,
             ext: str = "png") -> bool:
        """Save the retrieved image to a file.

        Save the image retrieved from Picsum to a file in given format. If
        no path is provided, or if path is a directory, a random filename
        will be created, and care will be taken to ensure that no files
        with the same name already exist. Otherwise, the image will be
        saved to the given filename (automatically appending the given
        format suffix).

        :param Optional[str] path: path/filename to save the image

        :param str ext: output file extension (default: png)

        :return: True
        """
        if ext not in ["png", "jpeg", "jpg"]:
            raise ValueError("Filetype not allowed." 
                             "Please provide either 'png', 'jpeg' or 'jpg'.")
        rnd_name = "{}.{}".format(self.random_string(), ext)
        if path:
            if os.path.isdir(path):
                while os.path.isfile(os.path.join(path, rnd_name)):
                    rnd_name = "{}.{}".format(self.random_string(), ext)
                self._filename = os.path.join(path, rnd_name)
            elif os.path.isfile(path):
                raise FileExistsError("File {} already exists!".format(path),
                                      "Please provide a different filename.")
            else:
                self._filename = path
        else:
            while os.path.isfile(rnd_name):
                rnd_name = "{}.{}".format(self.random_string(), ext)
            self._filename = rnd_name

        with open(self._filename, "wb") as f:
            f.write(self.pic)

        return True


