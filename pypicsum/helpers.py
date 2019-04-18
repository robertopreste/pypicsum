#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import random
from string import ascii_letters, digits


def random_string(length: int = 12) -> str:
    """Create a random string of the given length.

    Return a random alphanumeric string of the given length, which will
    be used for the image filename.
    :param int length: desired length of the random string (default: 12)
    :return: str
    """
    source = ascii_letters + digits

    return "".join([random.choice(source) for _ in range(length)])


