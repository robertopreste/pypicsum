#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import os


IMGDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imgs")


@pytest.fixture
def img_500x500_id_3():
    return os.path.join(IMGDIR, "img_500x500_id_3.png")


@pytest.fixture
def img_800x600_id_5():
    return os.path.join(IMGDIR, "img_800x600_id_5.png")


@pytest.fixture
def img_500x500_id_3_grayscale():
    return os.path.join(IMGDIR, "img_500x500_id_3_grayscale.png")


@pytest.fixture
def img_500x500_id_3_blur():
    return os.path.join(IMGDIR, "img_500x500_id_3_blur.png")


@pytest.fixture
def img_500x500_id_3_grayscale_blur():
    return os.path.join(IMGDIR, "img_500x500_id_3_grayscale_blur.png")
