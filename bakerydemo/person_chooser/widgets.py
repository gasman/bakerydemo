import json

from django.contrib.admin.utils import quote
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from bakerydemo.generic_chooser.widgets import AdminChooser

from bakerydemo.base.models import People


class AdminPersonChooser(AdminChooser):
    choose_one_text = _('Choose a person')
    choose_another_text = _('Choose another person')
    link_to_chosen_text = _('Edit this person')

    def render_html(self, name, value, attrs):
        instance, value = self.get_instance_and_id(People, value)
        original_field_html = super().render_html(name, value, attrs)

        if instance is None:
            edit_item_url = None
        else:
            edit_item_url = self.get_edit_item_url(instance)

        return render_to_string("generic_chooser/widgets/chooser.html", {
            'widget': self,
            'original_field_html': original_field_html,
            'attrs': attrs,
            'value': value,
            'item': instance,
            'edit_item_url': edit_item_url,
        })

    def get_edit_item_url(self, item):
        return reverse('wagtailsnippets:edit', args=('base', 'people', quote(item.pk)))

    def render_js_init(self, id_, name, value):
        return "createPersonChooser({0});".format(json.dumps(id_))

    class Media:
        js = [
            'js/person-chooser-modal.js',
            'js/person-chooser.js',
        ]
