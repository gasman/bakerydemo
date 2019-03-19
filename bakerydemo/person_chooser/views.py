from django.contrib.admin.utils import quote
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from bakerydemo.base.models import People
from bakerydemo.generic_chooser.views import ChooseView, ChosenView


class ChoosePersonView(ChooseView):
    icon = 'user'
    model = People
    page_title = _("Choose a person")
    chosen_url_name = 'person_chooser:chosen_person'


class ChosenPersonView(ChosenView):
    model = People

    def get_edit_url(self, item):
        return reverse('wagtailsnippets:edit', args=('base', 'people', quote(item.pk)))
