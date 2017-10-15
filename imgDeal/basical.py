# -*- coding: utf-8 -*-
from PIL import Image

class ACTransform(object):
    """docstring for transform."""
    def __init__(self, img):
        super(ACTransform, self).__init__()
        self.img = img

# 水平平移
    def roll(self,delta):
        xsize, ysize = self.img.size
        delta = delta % xsize

        if delta == 0:
            return self.img

        part1 = self.img.crop((0,0,delta,ysize))
        part2 = self.img.crop((delta,0,xsize,ysize))
        self.img.paste(part2,(0,0,xsize-delta,ysize))
        self.img.paste(part1,(xsize-delta,0,xsize,ysize))

        return self.img
