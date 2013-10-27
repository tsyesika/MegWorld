from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^servers/', 'MegWorld.views.servers', name='servers'),
    url(r'^$', 'MegWorld.views.home', name="Home"),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # match on page names /<page name>
    url(r'^(?P<name>\w+)/$', 'MegWorld.views.default', name='default'),
    # url(r'^MegWorld/', include('MegWorld.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
