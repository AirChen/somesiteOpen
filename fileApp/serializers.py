# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import LANGUAGE_CHOICES, STYLE_CHOICES, ImageItem

from StringIO import StringIO
from PIL import Image
#上级目录
import sys
sys.path.append("..")
from imgProcess.basical import ACTransform

from django.core.files.base import ContentFile
import base64
import six
import uuid
import imghdr
#https://stackoverflow.com/questions/28036404/django-rest-framework-upload-image-the-submitted-data-was-not-a-file
class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """
    def __init__(self,protype,**kwargs):
        self.protype = protype
        super(Base64ImageField, self).__init__(**kwargs)

    def to_internal_value(self, data):
        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )

            sbuf = StringIO()
            sbuf.write(decoded_file)
            pimg = Image.open(sbuf)

            #是否保存原图
            #pimg.save('static/fileApp/files/%s'%complete_file_name)

            #作为判断标志位
            print self.protype
            imgP = ACTransform(pimg)
            pimg = imgP.roll(120)

    #https://stackoverflow.com/questions/33754935/read-a-base-64-encoded-image-from-memory-using-opencv-python-library

            #需要还原data
            #https://stackoverflow.com/questions/46618746/how-to-transform-pil-image-object-to-buffer-string
            cimage = StringIO()
            pimg.seek(0)
            if file_extension == 'jpg':
                pimg.save(cimage,'jpeg')
            else:
                pimg.save(cimage,file_extension)
            contents = cimage.getvalue()

            data = ContentFile(contents, name=complete_file_name)
        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension
        return extension

class ImageItemSerializer(serializers.HyperlinkedModelSerializer):
    img = Base64ImageField(
        protype='平移',max_length=None, use_url=True,
    )
    class Meta:
        model = ImageItem
        fields = ('id', 'title', 'img')
