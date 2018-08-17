from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from blog.views import *


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', PostInBlog.as_view(), name='particular_blog'),
    url(r'^post/(?P<pk>\d+)/$', PostWithComments.as_view(),
        name='particular_post'),
    url(r'^(?P<pk>\d+)/new_post/$', login_required(NewPost.as_view()), name='new_post'),
    url(r'^post/(?P<pk>\d+)/edit/$', login_required(PostUpdate.as_view()), name='edit_post'),
    url(r'^(?P<pk>\d+)/edit/$', login_required(BlogUpdate.as_view()), name='edit_blog'),
    url(r'^new/$', login_required(NewBlog.as_view()), name='new_blog'),
    url(r'^$', BlogList.as_view(), name='blog_list'),
]
