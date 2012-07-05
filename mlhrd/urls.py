from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mlhrd.views.home', name='home'),
    # url(r'^mlhrd/', include('mlhrd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # used for logins 
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
        
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),                       
    url(r'^ner/', include('ner.urls')),
    url(r'^search/$',include('haystack.urls')),
    url(r'^comments/',include('django.contrib.comments.urls')),
)
