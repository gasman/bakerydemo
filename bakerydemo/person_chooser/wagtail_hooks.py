from django.conf.urls import include, url
from wagtail.core import hooks

from bakerydemo.person_chooser import admin_urls


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^people/', include(admin_urls, namespace='person_chooser')),
    ]
