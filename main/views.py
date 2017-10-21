# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response

# Create your views here.
class PartItem(object):
	"""docstring for PartItem."""
	def __init__(self,title,desc):
		super(PartItem, self).__init__()
		self.imgUrl = ''
		self.transUrl = ''
		self.title = title
		self.desc = desc

class Part(object):
	"""docstring for Part."""
	def __init__(self,name,desc):
		super(Part, self).__init__()
		self.name = name
		self.desc = desc
		self.items = []

def welcome(request):
	#return HttpResponse("<h1> Welcome to my tiny ImageSite! </h1>")
	web_name = '图像科技馆'
	web_headerImg_url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1505563774317&di=766c16eafe32f1c67c9b319032d5c5c5&imgtype=0&src=http%3A%2F%2Fwww.daoyouz.com%2Fpicture%2Fabed28443746d19e427bae2564cc19a4.jpg'

	part1 = Part('OpenCV技术展示','这里有很多很多的OpenCV实例可以了解，我们调研了很多的应用场景')
	item10 = PartItem('图像分割','这里有很多我们平常不容易看到的分割技术')
	item11 = PartItem('图像分割','这里有很多我们平常不容易看到的分割技术')
	item12 = PartItem('图像分割','这里有很多我们平常不容易看到的分割技术')
	part1.items = [item10,item11,item12]

	part2 = Part('OpenCV技术展示','这里有很多很多的OpenCV实例可以了解，我们调研了很多的应用场景')
	item20 = PartItem('图像分割','这里有很多我们平常不容易看到的分割技术')
	item21 = PartItem('图像分割','这里有很多我们平常不容易看到的分割技术')
	item22 = PartItem('图像分割','这里有很多我们平常不容易看到的分割技术')
	part2.items = [item20,item21,item22]

	part_list = [part1,part2]

	return render_to_response('welcome.html',{'web_name':web_name,'web_headerImg_url':web_headerImg_url,'part_list':part_list})
