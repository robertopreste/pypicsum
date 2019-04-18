#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import random
from pypicsum.helpers import random_string


def test_random_string():
    expect = "bRYxrzgWQRQh"
    random.seed(420)
    result = random_string()

    assert result == expect


def test_random_string_default_length():
    expect = 12
    result = len(random_string())

    assert result == expect


def test_random_string_custom_length():
    expect = 6
    result = len(random_string(6))

    assert result == expect
