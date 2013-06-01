# -*- coding: utf-8 -*-
from django.conf import settings


def site_pages(request):
    context = dict()
    if settings.DEPLOYMENT_MODE == 'dev':
        context['DEV_DEPLOYMENT_MODE'] = True

    context['COMPRESS_REVISION_NUMBER'] = settings.COMPRESS_REVISION_NUMBER
    context['MEDIA_URL'] = settings.MEDIA_URL

    context['RSS_FEED_URL'] = settings.RSS_FEED_URL
    context['RSS_FEED_ENABLED'] = settings.RSS_FEED_ENABLED

    context['TWITTER_INTEGRATION_ENABLED'] = settings.TWITTER_INTEGRATION_ENABLED
    context['GITHUB_INTEGRATION_ENABLED'] = settings.GITHUB_INTEGRATION_ENABLED
    context['DRIBBBLE_INTEGRATION_ENABLED'] = settings.DRIBBBLE_INTEGRATION_ENABLED
    context['INSTAGRAM_INTEGRATION_ENABLED'] = settings.INSTAGRAM_INTEGRATION_ENABLED
    context['BITBUCKET_INTEGRATION_ENABLED'] = settings.BITBUCKET_INTEGRATION_ENABLED
    context['LASTFM_INTEGRATION_ENABLED'] = settings.LASTFM_INTEGRATION_ENABLED
    context['SOUNDCLOUD_INTEGRATION_ENABLED'] = settings.SOUNDCLOUD_INTEGRATION_ENABLED
    context['FOURSQUARE_INTEGRATION_ENABLED'] = settings.FOURSQUARE_INTEGRATION_ENABLED

    context['TENT_INTEGRATION_ENABLED'] = settings.TENT_INTEGRATION_ENABLED
    context['TENT_ENTITY_URI'] = settings.TENT_ENTITY_URI
    context['TENT_FEED_URL'] = settings.TENT_FEED_URL

    context['STEAM_INTEGRATION_ENABLED'] = settings.STEAM_INTEGRATION_ENABLED
    context['STACKOVERFLOW_INTEGRATION_ENABLED'] = settings.STACKOVERFLOW_INTEGRATION_ENABLED

    context['FLICKR_INTEGRATION_ENABLED'] = settings.FLICKR_INTEGRATION_ENABLED
    context['FLICKR_ID'] = settings.FLICKR_ID

    context['DISQUS_INTEGRATION_ENABLED'] = settings.DISQUS_INTEGRATION_ENABLED
    context['DISQUS_SHORTNAME'] = settings.DISQUS_SHORTNAME

    context['DEMOS_INTEGRATION_ENABLED'] = settings.DEMOS_INTEGRATION_ENABLED

    context['GOOGLE_ANALYTICS_TRACKING_ID'] = settings.GOOGLE_ANALYTICS_TRACKING_ID
    context['SHARETHIS_PUBLISHER_KEY'] = settings.SHARETHIS_PUBLISHER_KEY

    context['WOOPRA_TRACKING_DOMAIN'] = settings.WOOPRA_TRACKING_DOMAIN
    context['WOOPRA_TRACKING_IDLE_TIMEOUT'] = settings.WOOPRA_TRACKING_IDLE_TIMEOUT
    context['WOOPRA_TRACKING_INCLUDE_QUERY'] = settings.WOOPRA_TRACKING_INCLUDE_QUERY

    context['blog_platform'] = settings.BLOG_PLATFORM
    context['wp_blog_url'] = settings.WORDPRESS_BLOG_URL

    return context
