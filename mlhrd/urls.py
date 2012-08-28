from django.conf.urls import patterns, include, url
import ner.models

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
        
    url(r'^admin/', include(admin.site.urls)),                       
    url(r'^ner/', include('ner.urls')),
    url(r'^search/$',include('haystack.urls')),
    url(r'^comments/',include('django.contrib.comments.urls')),
)
