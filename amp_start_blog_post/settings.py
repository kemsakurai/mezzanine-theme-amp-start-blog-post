# -*- coding: utf-8 -*-
from django.conf import settings as django_settings
import django

CACHE_LOADER_NAME = 'amp_start_blog_post.loaders.CachedLoader'
AMP_TOOLS_LOADER = 'amp_start_blog_post.loaders.Loader'


class SettingsProxy(object):
    def __init__(self, settings, defaults):
        self.settings = settings
        self.defaults = defaults

    def __getattr__(self, attr):
        try:
            return getattr(self.settings, attr)
        except AttributeError:
            try:
                return getattr(self.defaults, attr)
            except AttributeError:
                raise AttributeError(u'settings object has no attribute "%s"' % attr)


class defaults(object):

    AMP_TOOLS_TEMPLATE_FOLDER = u'amp_start_blog_post'
    AMP_TOOLS_TEMPLATE_PREFIX = ''
    AMP_TOOLS_TEMPLATE_LOADERS = []

    if django.VERSION[0] < 2 and django.VERSION[1] < 8:
        TEMPLATES = django_settings.TEMPLATE_LOADERS
    else:
        TEMPLATES = django_settings.TEMPLATES[0]['OPTIONS']['loaders']

    for loader in TEMPLATES:
        if isinstance(loader, (tuple, list)) and loader[0] == CACHE_LOADER_NAME:
            for cached_loader in loader[1]:
                if cached_loader != AMP_TOOLS_LOADER:
                    AMP_TOOLS_TEMPLATE_LOADERS.append(cached_loader)
        elif loader != AMP_TOOLS_LOADER:
            AMP_TOOLS_TEMPLATE_LOADERS.append(loader)
    AMP_TOOLS_TEMPLATE_LOADERS = tuple(AMP_TOOLS_TEMPLATE_LOADERS)

settings = SettingsProxy(django_settings, defaults)
