# -*- coding: utf-8 -*-
from PIL import Image, ImageFilter, ImageEnhance, PSDraw

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

        return self

    def toImage(self):
        return self.img
