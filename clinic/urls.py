from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	 url(r'^$', 'notetaker.views.home_page', name='home'),
	 url(r'^register/$', 'notetaker.views.register_user', name='register'),
	 url(r'^newnote/$', 'notetaker.views.newnote_page', name='newnote'),
	 url(r'^addpatient/$', 'notetaker.views.addpatient_page', name='addpatient'),
         url(r'^admin/', include(admin.site.urls)),
         url(r'^accounts/', include('registration.urls')),
         url(r'^ckeditor/', include('ckeditor.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)