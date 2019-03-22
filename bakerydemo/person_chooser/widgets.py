from django.contrib.admin.utils import quote
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

import requests

from wagtail.core.models import Page

from bakerydemo.base.models import People
from bakerydemo.generic_chooser.widgets import AdminChooser


class AdminPersonChooser(AdminChooser):
    choose_one_text = _('Choose a person')
    choose_another_text = _('Choose another person')
    link_to_chosen_text = _('Edit this person')
    model = People
    choose_modal_url_name = 'person_chooser:choose_person'

    def get_edit_item_url(self, item):
        return reverse('wagtailsnippets:edit', args=('base', 'people', quote(item.pk)))


class PageModelChooser(AdminChooser):
    choose_one_text = _('Choose a page')
    choose_another_text = _('Choose another page')
    link_to_chosen_text = _('Edit this page')
    model = Page
    choose_modal_url_name = 'person_chooser:choose_page'
    edit_item_url_name = 'wagtailadmin_pages:edit'


class PageAPIChooser(AdminChooser):
    choose_one_text = _('Choose a page')
    choose_another_text = _('Choose another page')
    link_to_chosen_text = _('Edit this page')
    choose_modal_url_name = 'person_chooser:choose_page'

    def get_instance(self, id):
        url = 'http://localhost:8000/api/v2/pages/%d/?format=json' % id
        return requests.get(url).json()

    def get_title(self, instance):
        if instance is None:
            return ''
        else:
            return instance['title']

    def get_edit_item_url(self, instance):
        return reverse('wagtailadmin_pages:edit', args=(instance['id'],))
