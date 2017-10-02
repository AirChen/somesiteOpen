# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
import os
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        #print '--->>' + form.Meta.model.objects.all()[0].files
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            moment = form.save()
            moment.save()
            return HttpResponse("<h1> Welcome to my tiny ImageSite! </h1>")
    else:
        form = ImageForm()
        return render_to_response('moments_input.html', {'form': form})

def html_file(request):
    return render_to_response('page_normal.html')
