#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
from pypicsum import Picsum


IMGDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "imgs")


def create_img_500x500_id_3():
    pic = Picsum(width=500, height=500, id_=3)
    try:
        pic.save(path=os.path.join(IMGDIR, "img_500x500_id_3.png"))
    except FileExistsError:
        os.remove(os.path.join(IMGDIR, "img_500x500_id_3.png"))
        pic.save(path=os.path.join(IMGDIR, "img_500x500_id_3.png"))
    return


def create_img_800x600_id_5():
    pic = Picsum(width=800, height=600, id_=5)
    try:
        pic.save(path=os.path.join(IMGDIR, "img_800x600_id_5.png"))
    except FileExistsError:
        os.remove(os.path.join(IMGDIR, "img_800x600_id_5.png"))
        pic.save(path=os.path.join(IMGDIR, "img_800x600_id_5.png"))
    return


def create_img_500x500_id_3_grayscale():
    pic = Picsum(width=500, height=500, id_=3, grayscale=True)
    try:
        pic.save(path=os.path.join(IMGDIR, "img_500x500_id_3_grayscale.png"))
    except FileExistsError:
        os.remove(os.path.join(IMGDIR, "img_500x500_id_3_grayscale.png"))
        pic.save(path=os.path.join(IMGDIR, "img_500x500_id_3_grayscale.png"))
    return


def create_img_500x500_id_3_blur():
    pic = Picsum(width=500, height=500, id_=3, blur=5)
    try:
        pic.save(path=os.path.join(IMGDIR, "img_500x500_id_3_blur.png"))
    except FileExistsError:
        os.remove(os.path.join(IMGDIR, "img_500x500_id_3_blur.png"))
        pic.save(path=os.path.join(IMGDIR, "img_500x500_id_3_blur.png"))
    return


def create_img_500x500_id_3_grayscale_blur():
    pic = Picsum(width=500, height=500, id_=3, grayscale=True, blur=3)
    try:
        pic.save(path=os.path.join(IMGDIR,
                                   "img_500x500_id_3_grayscale_blur.png"))
    except FileExistsError:
        os.remove(os.path.join(IMGDIR, "img_500x500_id_3_grayscale_blur.png"))
        pic.save(path=os.path.join(IMGDIR,
                                   "img_500x500_id_3_grayscale_blur.png"))
    return


def main():
    create_img_500x500_id_3()
    create_img_800x600_id_5()
    create_img_500x500_id_3_grayscale()
    create_img_500x500_id_3_blur()
    create_img_500x500_id_3_grayscale_blur()


if __name__ == '__main__':
    main()
