# -*- coding: utf-8 -*-
from PIL import Image, ImageFilter, ImageEnhance, PSDraw

from skimage.filters import roberts, sobel, scharr, prewitt
import numpy as np
import png
from matplotlib.pyplot import cm

class ACTransform(object):
    """docstring for transform."""
    def __init__(self, img):
        super(ACTransform, self).__init__()
        self.img = img

    # 水平平移
    def roll(self, delta):
        "Roll an image sideways"

        xsize, ysize = self.img.size

        delta = delta % xsize
        if delta == 0: return self.img

        part1 = self.img.crop((0, 0, delta, ysize))
        part2 = self.img.crop((delta, 0, xsize, ysize))
        part1.load()
        part2.load()
        self.img.paste(part2, (0, 0, xsize-delta, ysize))
        self.img.paste(part1, (xsize-delta, 0, xsize, ysize))

        return self

    def rotate(self, delta):
        self.img = self.img.rotate(delta)

        return self

    def resize(self, delta):
        self.img = self.img.resize((delta, delta))

        return self

    def flip_horizontal(self):
        self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)

        return self

    def flip_vertical(self):
        self.img = self.img.transpose(Image.FLIP_TOP_BOTTOM)

        return self

    # mark colors about.
    def filter(self):
        self.img = self.img.filter(ImageFilter.DETAIL)

        return self

    def points(self):
        self.img = self.img.point(lambda i: i * 1.2)

        return self

    # mark enhance
    def enhance(self, delta):
        enh = ImageEnhance.Contrast(self.img)
        self.img = enh.enhance(delta)
        print type(self.img)

        return self

    ###
    #image = Image.open(“ponzo.jpg”)   # image is a PIL image
    #array = numpy.array(image)          # array is a numpy array
    #image2 = Image.fromarray(array)   # image2 is a PIL image
    def ski_filter(self):
        im = list(self.img.getdata())
        robert_edge = roberts(im)
        im = Image.fromarray(cm.gist_earth(robert_edge, bytes=True))
        self.img = Image.new("RGB", im.size, (255,255,255))

        return self

    def toImage(self):
        return self.img
