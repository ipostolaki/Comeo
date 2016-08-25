from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.base.urls', namespace="base")),
    url(r'^profile/', include('apps.profiles.urls', namespace="profiles")),
    url(r'^crowdfunding/', include('apps.crowdfunding.urls', namespace="crowdfunding")),
    url(r'^registry/', include('apps.registry.urls', namespace="registry")),
    url(r'^ckeditor/', include('ckeditor.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)