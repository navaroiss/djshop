"""
URLConf for Django user registration and authentication.

Recommended usage is a call to ``include()`` in your project's root
URLConf to include this URLConf for any URL beginning with
``/accounts/``.

"""


from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views
from views import *
urlpatterns = patterns('',
                       # Activation keys get matched by \w+ instead of the more specific
                       # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
                       # that way it can return a sensible "invalid key" message instead of a
                       # confusing 404.
                       
                       url(r'/account/login/$',
                           auth_views.login,
                           {'template_name': 'registration/login.html'},
                           name='auth_login'),
                       url(r'/account/logout/$',
                           auth_views.logout,
                           {'template_name': 'registration/logout.html'},
                           name='auth_logout'),
                       url(r'^password_change/$',
                           auth_views.password_change,
                           name='auth_password_change'),
                       url(r'^password_change/done/$',
                           auth_views.password_change_done,
                           name='auth_password_change_done'),
                       url(r'^password_reset/$',
                           auth_views.password_reset,
                           name='auth_password_reset'),
                       url(r'account/forgotpassword/$', auth_views.password_reset, {'template_name': 'registration/forgotpassword.html'}, name='auth_password_reset'),
                       url(r'^password_reset/done/$',
                           auth_views.password_reset_done,
                           name='auth_password_reset_done'),
                       url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           auth_views.password_reset_confirm,
                           name='auth_password_reset_confirm'), 
                       url(r'^reset/done/$',
                           auth_views.password_reset_complete,
                           name='auth_password_reset_complete'), 
                       url(r'/account/register/$',
                           register, {'template_name':'registration/register.html'}),
                       url(r'^register/complete/$',
                           direct_to_template,
                           {'template': 'registration/registration_complete.html'}, name='registration_complete'),
                       )