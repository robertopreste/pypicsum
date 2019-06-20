#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import os
from click.testing import CliRunner
from pypicsum import cli
from tests.diff_finder import equal_imgs

IMGDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imgs")
TESTIMG = os.path.join(IMGDIR, "test_img.png")


def test_img_500x500_id_3(img_500x500_id_3):
    """Test retrieval of a 500x500 img with id 3."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["-W", "500", "-H", "500",
                                      "-i", "3", "-s", TESTIMG])
    assert result.exit_code == 0
    assert equal_imgs(img_500x500_id_3, TESTIMG)


def test_img_800x600_id_5(img_800x600_id_5):
    """Test retrieval of a 800x600 img with id 5."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["-W", "800", "-H", "600",
                                      "-i", "5", "-s", TESTIMG])
    assert result.exit_code == 0
    assert equal_imgs(img_800x600_id_5, TESTIMG)


def test_img_500x500_id_3_grayscale(img_500x500_id_3_grayscale):
    """Test retrieval of a 500x500 img in grayscale with id 3."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["-W", "500", "-H", "500",
                                      "-i", "3", "-g", "-s", TESTIMG])
    assert result.exit_code == 0
    assert equal_imgs(img_500x500_id_3_grayscale, TESTIMG)


def test_img_500x500_id_3_blur(img_500x500_id_3_blur):
    """Test retrieval of a 500x500 img blurred with id 3."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["-W", "500", "-H", "500",
                                      "-i", "3", "-b", "5",
                                      "-s", TESTIMG])
    assert result.exit_code == 0
    assert equal_imgs(img_500x500_id_3_blur, TESTIMG)


def test_img_500x500_id_3_grayscale_blur(img_500x500_id_3_grayscale_blur):
    """Test retrieval of a 500x500 img in grayscale and blurred with id 3."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["-W", "500", "-H", "500",
                                      "-i", "3", "-b", "3", "-g",
                                      "-s", TESTIMG])
    assert result.exit_code == 0
    assert equal_imgs(img_500x500_id_3_grayscale_blur, TESTIMG)


def teardown_function():
    os.remove(TESTIMG)

