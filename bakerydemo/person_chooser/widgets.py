import json

from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.widgets import AdminChooser

from bakerydemo.base.models import People


class AdminPersonChooser(AdminChooser):
    choose_one_text = _('Choose a person')
    choose_another_text = _('Choose another person')
    link_to_chosen_text = _('Edit this person')

    def render_html(self, name, value, attrs):
        instance, value = self.get_instance_and_id(People, value)
        original_field_html = super().render_html(name, value, attrs)

        return render_to_string("person_chooser/widgets/person_chooser.html", {
            'widget': self,
            'original_field_html': original_field_html,
            'attrs': attrs,
            'value': value,
            'item': instance,
        })

    def render_js_init(self, id_, name, value):
        return "createPersonChooser({0});".format(json.dumps(id_))

    class Media:
        js = [
            'js/person-chooser-modal.js',
            'js/person-chooser.js',
        ]
