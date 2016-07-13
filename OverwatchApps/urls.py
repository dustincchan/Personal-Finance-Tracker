from django.conf.urls import include, url
from django.contrib import admin
from .views import ApiEndpoint

urlpatterns = [
    # Examples:
    # url(r'^$', 'OverwatchApps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', 'OverwatchApps.views.login', name='login'),
]
