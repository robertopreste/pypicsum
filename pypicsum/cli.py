#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import sys
import click
from pypicsum.helpers import Picsum


@click.command()
@click.option("--width", "-W", default=500,
              help="""Width of the image (default: 500)""")
@click.option("--height", "-H", default=None,
              help="""Height of the image, if not provided returns a square 
              image (default: None)""")
@click.option("--random", "-r", is_flag=True, default=True,
              help="""Return a random image (default: True)""")
@click.option("--grayscale", "-g", is_flag=True, default=False,
              help="""Return the grayscale version of the image 
              (default: False)""")
@click.option("--blurred", "-b", is_flag=True, default=False,
              help="""Return the blurred version of the image 
              (default: False)""")
@click.option("--gravity", "-G", default=None,
              help="""Gravity crop of the image, accepts one of 'north', 
              'east', 'south', 'west', 'center' (default: False)""")
@click.option("--save_path", "-p", default=None,
              help="""Path/filename to save the image.""")
@click.option("--save_ext", "-e", default="png",
              help="""Output file extension (default: png)""")
@click.option("--show_url", "-u", is_flag=True, default=False,
              help="""Return the url used to retrieve the image 
              (default: False)""")
def main(width, height, random, grayscale, blurred, gravity,
         save_path, save_ext, show_url):
    """
    Retrieve an image from picsum.photos and save it.
    """
    p = Picsum(width, height, random, grayscale, blurred, gravity)
    p.save(save_path, save_ext)
    click.echo("Image saved to {}".format(p.filename))
    if show_url:
        click.echo("Image retrieved from {}".format(p.url))

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
