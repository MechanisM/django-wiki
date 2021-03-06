# -*- coding: utf-8 -*-

from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured
import warnings

# TODO: Don't use wildcards
from article import *
from urlpath import *

######################
# Configuration stuff
######################

if not 'mptt' in django_settings.INSTALLED_APPS:
    raise ImproperlyConfigured('django-wiki: needs mptt in INSTALLED_APPS')

if not 'sekizai' in django_settings.INSTALLED_APPS:
    raise ImproperlyConfigured('django-wiki: needs sekizai in INSTALLED_APPS')

if not 'django.contrib.contenttypes' in django_settings.INSTALLED_APPS:
    raise ImproperlyConfigured('django-wiki: needs django.contrib.contenttypes in INSTALLED_APPS')

if not 'django.contrib.auth.context_processors.auth' in django_settings.TEMPLATE_CONTEXT_PROCESSORS:
    raise ImproperlyConfigured('django-wiki: needs django.contrib.auth.context_processors.auth in TEMPLATE_CONTEXT_PROCESSORS')

######################
# Warnings
######################

if not 'south' in django_settings.INSTALLED_APPS:
    warnings.warn("django-wiki: No south in your INSTALLED_APPS. This is highly discouraged.")
    