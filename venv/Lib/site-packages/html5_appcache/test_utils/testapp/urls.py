# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

import html5_appcache
html5_appcache.autodiscover()

from .sitemap import NewsSitemap
from .views import NewsListView, NewsDetailView

sitemaps = {
    'news': NewsSitemap,
}

urlpatterns = i18n_patterns('',
    url("^list/$", NewsListView.as_view(), name="news_list"),
    url("^(?P<pk>\d+)/live/$", NewsListView.as_view(), name="news_detail_live"),
    url("^(?P<pk>\d+)/$", NewsDetailView.as_view(), name="news_detail"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)
if html5_appcache.settings.DJANGOCMS:
    urlpatterns += i18n_patterns('',
        url(r'^', include('cms.urls')),
    )