from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from notetaker.views import (ExampleSecretView, RegistrationView,RegistrationCompleteView)
from django.contrib import admin
from two_factor.urls import urlpatterns as tf_urls
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls
from notetaker.views import SecureView
from two_factor.admin import AdminSiteOTPRequired
from two_factor.views import LoginView
admin.autodiscover()


urlpatterns = patterns('',
	 url(r'^$', 'notetaker.views.home_page', name='home'),
         url(r'^newnote/$', 'notetaker.views.newnote_page', name='newnote'),
	 url(r'^addpatient/$', 'notetaker.views.addpatient_page', name='addpatient'),
         url(regex=r'^account/logout/$',view='django.contrib.auth.views.logout',name='logout',),
         url(regex=r'^account/custom-login/$',view=LoginView.as_view(redirect_field_name='next_page'),name='custom-login',),
         url(regex=r'^secret/$',view=ExampleSecretView.as_view(),name='secret',),
         url(regex=r'^account/register/$',view=RegistrationView.as_view(),name='registration',),
         url(regex=r'^account/register/done/$',view=RegistrationCompleteView.as_view(),name='registration_complete',),
         url(r'^accounts/', include('registration.urls')),
         url(r'^ckeditor/', include('ckeditor.urls')),
         url(regex=r'^secure/$',view=SecureView.as_view(),),
         url(regex=r'^secure/raises/$',view=SecureView.as_view(raise_anonymous=True, raise_unverified=True),),
         url(regex=r'^secure/redirect_unverified/$',
         view=SecureView.as_view(raise_anonymous=True,verification_url='/account/login/'),),
         url(r'', include('two_factor.urls', 'two_factor')),
         url(r'', include('user_sessions.urls', 'user_sessions')),
         url(r'', include(tf_urls + tf_twilio_urls, 'two_factor')),
         url(r'^admin/', include(admin.site.urls)),
         #url(r'^otp_admin/', include(otp_admin_site.urls)),

        
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)