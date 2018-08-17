from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from blog.views import NewBlog
from core.views import *


urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name='core/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='core/base.html'), name='logout'),
    url(r'^register/$', register_user, name='register'),
    url(r'^profile/(?P<person_name>\w+)/$', profile),
]
