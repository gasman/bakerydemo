import json

from django.contrib.admin.utils import quote
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from bakerydemo.generic_chooser.widgets import AdminChooser

from bakerydemo.base.models import People


class AdminPersonChooser(AdminChooser):
    choose_one_text = _('Choose a person')
    choose_another_text = _('Choose another person')
    link_to_chosen_text = _('Edit this person')
    model = People
    choose_modal_url_name = 'person_chooser:choose_person'

    def get_edit_item_url(self, item):
        return reverse('wagtailsnippets:edit', args=('base', 'people', quote(item.pk)))

    def render_js_init(self, id_, name, value):
        return "createPersonChooser({0});".format(json.dumps(id_))

    class Media:
        js = [
            'js/person-chooser-modal.js',
            'js/person-chooser.js',
        ]
