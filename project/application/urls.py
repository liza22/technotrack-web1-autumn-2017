from django.conf.urls import url, include
from django.contrib import admin
from core.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'', include('core.urls')),
    url(r'blogs/', include('blog.urls', namespace='blogs')),
]
