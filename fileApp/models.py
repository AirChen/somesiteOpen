# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField
from versatileimagefield.placeholder import OnStoragePlaceholderImage

class ImageExampleModel(models.Model):
    name = models.CharField(
        'Name',
        max_length=80
    )
    image = VersatileImageField(
        'Image',
        upload_to='images/testimagemodel/',
        width_field='width',
        height_field='height',
        ppoi_field='ppoi'
    )
    height = models.PositiveIntegerField(
        'Image Height',
        blank=True,
        null=True
    )
    width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True
    )
    optional_image = VersatileImageField(
        'Optional Image',
        upload_to='images/testimagemodel/optional/',
        blank=True,
        placeholder_image=OnStoragePlaceholderImage(
            path='images/bear.jpg'
        )
    )
    ppoi = PPOIField()

    class Meta:
        verbose_name = 'Image Example'
        verbose_name_plural = 'Image Examples'
