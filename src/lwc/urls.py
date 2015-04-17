from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lwc.views.test', name='test'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'joins.views.home', name='home'),
    #url(r'^testhome$', 'lwc.views.testhome', name='testhome'),
    url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'),
)