from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main/', views.upload_file),
    url(r'^trans/', views.html_file),
]
