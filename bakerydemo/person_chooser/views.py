from django.contrib.admin.utils import quote
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from wagtail.core.models import Page

from bakerydemo.base.models import People
from bakerydemo.generic_chooser.views import DRFChooseView, ModelChooseView, DRFChosenView, ModelChosenView


class ChoosePersonView(ModelChooseView):
    icon = 'user'
    model = People
    page_title = _("Choose a person")
    choose_url_name = 'person_chooser:choose_person'
    chosen_url_name = 'person_chooser:chosen_person'


class ChosenPersonView(ModelChosenView):
    model = People

    def get_edit_item_url(self, item):
        return reverse('wagtailsnippets:edit', args=('base', 'people', quote(item.pk)))


class ChoosePageModelView(ModelChooseView):
    icon = 'page'
    model = Page
    page_title = _("Choose a page")
    choose_url_name = 'person_chooser:choose_page'
    chosen_url_name = 'person_chooser:chosen_page'


class ChoosePageAPIView(DRFChooseView):
    icon = 'page'
    page_title = _("Choose a page")
    choose_url_name = 'person_chooser:choose_page'
    chosen_url_name = 'person_chooser:chosen_page'
    api_base_url = 'http://localhost:8000/api/v2/pages/'

    def get_object_string(self, item):
        return item['title']


class ChosenPageModelView(ModelChosenView):
    model = Page
    edit_item_url_name = 'wagtailadmin_pages:edit'


class ChosenPageAPIView(DRFChosenView):
    edit_item_url_name = 'wagtailadmin_pages:edit'
    api_base_url = 'http://localhost:8000/api/v2/pages/'

    def get_object_string(self, item):
        return item['title']
