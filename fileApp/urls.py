from django.conf.urls import url,include

# from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    #url(r'^main/', views.upload_file),
    url(r'^trans/', views.html_file),

    url(r'^$', views.SnippetList.as_view()),
    url(r'^(?P<pk>[0-9]+)$', views.SnippetDetail.as_view()),

    # url(r'^', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
