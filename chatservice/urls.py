from django.conf.urls import include, url
from django.contrib import admin

from chat_main.views import index
from chat_main.urls import urlpatterns as chat_urlpatterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'chatservice.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index),
    url(r'^api/', include(chat_urlpatterns)),

    url(r'^admin/', include(admin.site.urls)),
]

