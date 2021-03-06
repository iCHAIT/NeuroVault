from neurovault.api.sitemap import CollectionSitemap, ImageSitemap, CognitiveAtlasTaskSitemap
from django.conf.urls import include, patterns, url
from oauth2_provider import views as oauth_views
from django.contrib.sitemaps.views import sitemap
from neurovault.api.urls import api_urls
from django.conf import settings
from django.contrib import admin
import os

admin.autodiscover()

sitemaps = {"Collections":CollectionSitemap,
            "Images":ImageSitemap,
            "CognitiveAtlasTasks":CognitiveAtlasTaskSitemap}

oauth_urlpatterns = [
    url(r'^authorize/$', oauth_views.AuthorizationView.as_view(),
        name="authorize"),
    url(r'^token/$', oauth_views.TokenView.as_view(),
        name="token"),
    url(r'^revoke_token/$', oauth_views.RevokeTokenView.as_view(),
        name="revoke-token"),
]

urlpatterns = patterns('',
                       url('', include(
                           'social.apps.django_app.urls', namespace='social')),
                       url(r'^', include('neurovault.apps.main.urls')),
                       url(r'^', include('neurovault.apps.statmaps.urls')),
                       url(r'^accounts/',
                           include('neurovault.apps.users.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include(api_urls)),
                       url(r'^api-auth/', include(
                           'rest_framework.urls', namespace='rest_framework')),
                       url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
                           name='django.contrib.sitemaps.views.sitemap'),
                       url(r'^o/', include((oauth_urlpatterns,
                                            'oauth2_provider',
                                            'oauth2_provider'))),
                       )

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^(?P<path>favicon\.ico)$', 'django.views.static.serve', {
            'document_root': os.path.join(settings.STATIC_ROOT, 'images')}),
    )
