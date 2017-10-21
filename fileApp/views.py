# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
import os
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from models import ImageItem
from serializers import ImageItemSerializer

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

from rest_framework.views import APIView
from rest_framework import generics

from django.contrib.auth.models import User
from permissions import IsOwnerOrReadOnly

class ImageItemsList(generics.ListCreateAPIView):
    queryset = ImageItem.objects.all()
    serializer_class = ImageItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ImageItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageItem.objects.all()
    serializer_class = ImageItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

def html_file(request):
    return render_to_response('page_normal.html')
