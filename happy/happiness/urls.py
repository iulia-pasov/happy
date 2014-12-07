from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'happiness.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^test/$', 'happiness.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
)