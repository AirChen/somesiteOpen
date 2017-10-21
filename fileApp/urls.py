from django.conf.urls import url,include

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #url(r'^main/', views.upload_file),
    url(r'^trans/', views.html_file),

    url(r'^images/$', views.ImageItemsList.as_view()),
    url(r'^images/(?P<pk>[0-9]+)$', views.ImageItemsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
