from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from menu_list import views
 

urlpatterns = [
    url(r'^menu/$', views.MenuList.as_view(), name='menu-list'),
    url(r'^menu/(?P<pk>[0-9]+)/$', views.MenuDetail.as_view(), name='menu-detail'),
]