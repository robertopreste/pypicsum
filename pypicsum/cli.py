#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import sys
import click
from pypicsum.classes import Picsum


@click.command()
@click.option("--width", "-W", default=500,
              help="""Width of the image (default: 500)""")
@click.option("--height", "-H", default=None,
              help="""Height of the image, if not provided returns a square 
              image (default: None)""")
@click.option("--image", "-i", default=None, type=int,
              help="""Return a specific image instead of a random one 
              (default: None)""")
@click.option("--grayscale", "-g", is_flag=True, default=False,
              help="""Return the grayscale version of the image 
              (default: False)""")
@click.option("--blur", "-b", default=None, type=int,
              help="""Return the blurred version of the image and optionally 
              select a blurring value between 1 and 10 (default: False)""")
@click.option("--save_path", "-s", default=None,
              help="""Path/filename to save the image 
              (default: random string in current path).""")
@click.option("--save_ext", "-e", default="png",
              type=click.Choice(["png", "jpeg", "jpg"]),
              help="""Output file extension (default: png)""")
@click.option("--show_url", "-u", is_flag=True, default=False,
              help="""Return the url used to retrieve the image 
              (default: False)""")
def main(width, height, image, grayscale, blur,
         save_path, save_ext, show_url):
    """Retrieve an image from picsum.photos and save it."""
    p = Picsum(width, height, image, grayscale, blur)
    p.save(save_path, save_ext)
    click.echo("Image saved to {}".format(p.filename))
    if show_url:
        click.echo("Image retrieved from {}".format(p.url))

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
