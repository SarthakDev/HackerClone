from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth
from links.views import LinkListView, UserProfileDetailView, UserProfileEditView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'hackerclone.views.home', name='home'),
                       # url(r'^hackerclone/', include('hackerclone.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', LinkListView.as_view(), name='home'),
                       url(r'^login/$', 'django.contrib.auth.views.login', {
                           'template_name': 'login.html'}, name='login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
                       url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name='profile'),
                       url(r'^edit_profile/$', auth(UserProfileEditView.as_view()), name='edit_profile'),
                       url(r'^accounts/', include('registration.backends.simple.urls')),
                       )
