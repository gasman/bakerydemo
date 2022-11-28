from django.contrib.admin.utils import quote
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from generic_chooser.widgets import AdminChooser

from bakerydemo.base.models import Person


class PersonChooser(AdminChooser):
    choose_one_text = _("Choose a person")
    choose_another_text = _("Choose another person")
    link_to_chosen_text = _("Edit this person")
    model = Person
    choose_modal_url_name = "person_chooser:choose"

    def get_edit_item_url(self, item):
        return reverse("wagtailsnippets:edit", args=("base", "person", quote(item.pk)))
