from django.contrib.admin.utils import quote
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

import requests

from wagtail.core.models import Page

from bakerydemo.base.models import People
from bakerydemo.generic_chooser.views import ChooseView, ChosenView


class ChoosePersonView(ChooseView):
    icon = 'user'
    model = People
    page_title = _("Choose a person")
    chosen_url_name = 'person_chooser:chosen_person'


class ChosenPersonView(ChosenView):
    model = People

    def get_edit_item_url(self, item):
        return reverse('wagtailsnippets:edit', args=('base', 'people', quote(item.pk)))


class ChoosePageModelView(ChooseView):
    icon = 'page'
    model = Page
    page_title = _("Choose a page")
    chosen_url_name = 'person_chooser:chosen_page'


class ChosenPageModelView(ChosenView):
    model = Page
    edit_item_url_name = 'wagtailadmin_pages:edit'


class ChosenPageAPIView(ChosenView):
    def get_object(self, id):
        url = 'http://localhost:8000/api/v2/pages/%s/?format=json' % quote(id)
        result = requests.get(url).json()

        if 'id' not in result:
            # assume this is a 'not found' report
            raise ObjectDoesNotExist(result['message'])

        return result

    def get_response_data(self, item):
        return {
            'id': str(item['id']),
            'string': str(item['title']),
            'edit_link': self.get_edit_item_url(item)
        }

    def get_edit_item_url(self, instance):
        return reverse('wagtailadmin_pages:edit', args=(instance['id'],))
