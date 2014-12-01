from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    #url(r'^app_name/', include('app_name.urls', namespace='app_name')),
    url(r'^admin/', include(admin.site.urls)),
)
