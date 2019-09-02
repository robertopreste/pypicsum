#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import cv2
import numpy as np


def equal_imgs(img_1: str, img_2: str) -> bool:
    """Test whether or not two images are the same.

    Compare two images and determine if they are equal, considering their
    size and blue, green, red channels.

    Args:
        img_1 (str): first image path
        img_2 (str): second image path

    Returns:
        bool
    """

    original = cv2.imread(img_1)
    tester = cv2.imread(img_2)

    if original.shape == tester.shape:
        diff = cv2.subtract(original, tester)
        b, g, r = cv2.split(diff)
        if cv2.countNonZero(b) == 0 and \
            cv2.countNonZero(g) == 0 and \
            cv2.countNonZero(r) == 0:
            return True

    return False

