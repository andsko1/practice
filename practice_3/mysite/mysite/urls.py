from django.conf.urls import *
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^log/(?P<path>.*)$', 'papages.views.listing'),
    url(r'^$', 'papages.views.home'),
    url(r'^library/$', 'books.views.books'),	
    url(r'^library/books/$', 'books.views.books'),
    url(r'^library/books/(?P<book>\d+)/$', 'books.views.book'),
    url(r'^library/authors/$', 'books.views.authors'),
    url(r'^library/authors/(?P<author>\d+)/$', 'books.views.author'),
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
