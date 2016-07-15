from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('comeo_app.urls', namespace="comeo_app")),
    url(r'^registry/', include('registry.urls', namespace="registry")),
    url(r'^ckeditor/', include('ckeditor.urls')),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)