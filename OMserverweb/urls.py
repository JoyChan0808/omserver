from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OMserverweb.views.home', name='home'),
    # url(r'^OMserverweb/', include('OMserverweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^autoadmin/', include('autoadmin.urls')),
    url(r'^$','autoadmin.views.index'), 
#    url(r'^autoadmin/module_add$','autoadmin.views.module_add'),
)