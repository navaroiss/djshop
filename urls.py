from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth import views as auth_views

from views import home_page 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^djshop/', include('djshop.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    ('^$', home_page),
    ('^customer', include('djshop.shopapps.registration.urls'))
)
