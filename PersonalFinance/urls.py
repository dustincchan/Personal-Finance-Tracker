from django.conf.urls import include, url
from django.contrib import admin, auth
from django.views.generic import RedirectView
import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^login/$', auth.views.login),
    url(r'^logout/$', auth.views.logout),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/')),
]
