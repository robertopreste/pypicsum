#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import os
from pypicsum.classes import Picsum
from tests.diff_finder import equal_imgs

IMGDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imgs")
TESTIMG = os.path.join(IMGDIR, "test_img.png")


class TestImg500x500Id3:
    p = Picsum(width=500, id_=3)

    def test_request_url(self):
        """Test the request URL generated by the Picsum class."""
        expect = "https://picsum.photos/id/3/500"
        result = self.p.request_url
        assert result == expect

    def test_url(self):
        """Test the actual URL returned by picsum.photos."""
        expect = "https://picsum.photos/id/3/500/500"
        result = self.p.url
        assert result == expect

    def test_image(self, img_500x500_id_3):
        """Test the actual image returned."""
        self.p.save(TESTIMG)
        assert equal_imgs(img_500x500_id_3, TESTIMG)

    @classmethod
    def teardown_class(cls):
        os.remove(TESTIMG)


class TestImg800x600Id5:
    p = Picsum(width=800, height=600, id_=5)

    def test_request_url(self):
        """Test the request URL generated by the Picsum class."""
        expect = "https://picsum.photos/id/5/800/600"
        result = self.p.request_url
        assert result == expect

    def test_url(self):
        """Test the actual URL returned by picsum.photos."""
        expect = "https://picsum.photos/id/5/800/600"
        result = self.p.url
        assert result == expect

    def test_image(self, img_800x600_id_5):
        """Test the actual image returned."""
        self.p.save(TESTIMG)
        assert equal_imgs(img_800x600_id_5, TESTIMG)

    @classmethod
    def teardown_class(cls):
        os.remove(TESTIMG)


class TestImg500x500Id3Grayscale:
    p = Picsum(width=500, id_=3, grayscale=True)

    def test_request_url(self):
        """Test the request URL generated by the Picsum class."""
        expect = "https://picsum.photos/id/3/500/?grayscale"
        result = self.p.request_url
        assert result == expect

    def test_url(self):
        """Test the actual URL returned by picsum.photos."""
        expect = "https://picsum.photos/id/3/500/500?grayscale"
        result = self.p.url
        assert result == expect

    def test_image(self, img_500x500_id_3_grayscale):
        """Test the actual image returned."""
        self.p.save(TESTIMG)
        assert equal_imgs(img_500x500_id_3_grayscale, TESTIMG)

    @classmethod
    def teardown_class(cls):
        os.remove(TESTIMG)


class TestImg500x500Id3Blur:
    p = Picsum(width=500, id_=3, blur=5)

    def test_request_url(self):
        """Test the request URL generated by the Picsum class."""
        expect = "https://picsum.photos/id/3/500/?blur=5"
        result = self.p.request_url
        assert result == expect

    def test_url(self):
        """Test the actual URL returned by picsum.photos."""
        expect = "https://picsum.photos/id/3/500/500?blur=5"
        result = self.p.url
        assert result == expect

    def test_image(self, img_500x500_id_3_blur):
        """Test the actual image returned."""
        self.p.save(TESTIMG)
        assert equal_imgs(img_500x500_id_3_blur, TESTIMG)

    @classmethod
    def teardown_class(cls):
        os.remove(TESTIMG)


class TestImg500x500Id3GrayscaleBlur:
    p = Picsum(width=500, id_=3, grayscale=True, blur=3)

    def test_request_url(self):
        """Test the request URL generated by the Picsum class."""
        expect = "https://picsum.photos/id/3/500/?grayscale&blur=3"
        result = self.p.request_url
        assert result == expect

    def test_url(self):
        """Test the actual URL returned by picsum.photos."""
        expect = "https://picsum.photos/id/3/500/500?blur=3&grayscale"
        result = self.p.url
        assert result == expect

    def test_image(self, img_500x500_id_3_grayscale_blur):
        """Test the actual image returned."""
        self.p.save(TESTIMG)
        assert equal_imgs(img_500x500_id_3_grayscale_blur, TESTIMG)

    @classmethod
    def teardown_class(cls):
        os.remove(TESTIMG)


class TestImg800x600Id5Jpg:
    p = Picsum(width=800, height=600, id_=5)

    def test_request_url(self):
        """Test the request URL generated by the Picsum class."""
        expect = "https://picsum.photos/id/5/800/600"
        result = self.p.request_url
        assert result == expect

    def test_url(self):
        """Test the actual URL returned by picsum.photos."""
        expect = "https://picsum.photos/id/5/800/600"
        result = self.p.url
        assert result == expect

    def test_image(self, img_800x600_id_5_jpg):
        """Test the actual image returned."""
        self.p.save(TESTIMG, ext="jpg")
        assert equal_imgs(img_800x600_id_5_jpg, TESTIMG)

    @classmethod
    def teardown_class(cls):
        os.remove(TESTIMG)


class TestImg800x600Id5Jpeg:
    p = Picsum(width=800, height=600, id_=5)

    def test_request_url(self):
        """Test the request URL generated by the Picsum class."""
        expect = "https://picsum.photos/id/5/800/600"
        result = self.p.request_url
        assert result == expect

    def test_url(self):
        """Test the actual URL returned by picsum.photos."""
        expect = "https://picsum.photos/id/5/800/600"
        result = self.p.url
        assert result == expect

    def test_image(self, img_800x600_id_5_jpeg):
        """Test the actual image returned."""
        self.p.save(TESTIMG, ext="jpeg")
        assert equal_imgs(img_800x600_id_5_jpeg, TESTIMG)

    @classmethod
    def teardown_class(cls):
        os.remove(TESTIMG)
