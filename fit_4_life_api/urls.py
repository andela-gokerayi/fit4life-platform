from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

from fit_4_life_api import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'api_root_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Fit4Life API', description='RESTful API for Fit4Life')),
    url(r'^$', views.api_root),
    url(r'^', include('users.urls', namespace='users')),
    url(r'^', include('menu_list.urls', namespace='menu')),
]
